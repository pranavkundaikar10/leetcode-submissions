class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        buckets = defaultdict(set)
        wordList = set(wordList)
        wordList.add(beginWord)
        print(wordList)
        adj = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                wildcard = word[:i] + "*" + word[i+1:]
                buckets[wildcard].add(word)
                adj[word].add(wildcard)
                # print(wildcard)

        queue = deque([(1, beginWord)])
        # print(adj)
        # print(buckets)

        visited = set()
        while queue:
            count, word = queue.popleft()
            # print(word)
            if word == endWord:
                return count
            if word in visited:
                continue
            visited.add(word)
            for bucket in adj[word]:
                for w in buckets[bucket]:
                    if w not in visited:
                        queue.append((1+count, w))
                buckets[bucket] = set()
            # print(buckets)
        return 0

