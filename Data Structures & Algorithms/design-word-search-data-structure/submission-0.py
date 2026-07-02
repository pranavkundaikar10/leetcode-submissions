class TrieNode:

    def __init__(self):
        self.children = [0] * 26
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.word = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in curr.children:
                        if child and dfs(j+1, child):
                            return True
                    return False
                else:
                    idx = ord(word[j]) - ord('a')
                    if not curr.children[idx]:
                        return False
                    curr = curr.children[idx]
            return curr.word

        return dfs(0, self.root)
        
