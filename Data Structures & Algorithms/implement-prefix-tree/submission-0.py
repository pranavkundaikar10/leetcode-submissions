class TrieNode:

    def __init__(self):
        self.children = [False] * 26
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.word = True


    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return curr.word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                return False
            curr = curr.children[idx]
        return True
        