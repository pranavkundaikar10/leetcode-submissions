class Trie:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        res = set()
        visited = set()
        root = Trie()
        for word in words:
            root.add_word(word)

        def dfs(r, c, node, word):
            if min(r, c) < 0 or r >= rows or c >= cols or board[r][c] not in node.children or (r, c) in visited:
                return
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.endOfWord:
                res.add(str(word))

            visited.add((r, c))
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            visited.remove((r, c))                         



        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)






        