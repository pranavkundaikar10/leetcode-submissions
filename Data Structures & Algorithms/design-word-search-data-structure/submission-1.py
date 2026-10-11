class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.endOfWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children:
                        if not child:
                            continue
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
            return curr.endOfWord
        return dfs(0, self.root)
        
