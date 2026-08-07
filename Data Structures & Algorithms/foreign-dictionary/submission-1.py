class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        indegree = {c:0 for c in adj}
        res = ""

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            print(f'{w1, w2}')
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegree[c2] += 1
                    break
        queue = deque([c for c in indegree if indegree[c] == 0])

        while queue:
            c = queue.popleft()
            res += c
            for j in adj[c]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
        if len(res) != len(indegree):
            return ""

        return res