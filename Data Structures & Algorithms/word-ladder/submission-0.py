class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        comboDict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                comboDict[pattern].append(word)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, length = queue.popleft()
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                for neighbor in comboDict[pattern]:
                    if neighbor == endWord:
                        return length + 1
                    
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, length+1))
                comboDict[pattern] = []
        return 0
    