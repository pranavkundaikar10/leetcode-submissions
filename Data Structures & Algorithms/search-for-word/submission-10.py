class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, j, curr):
            nonlocal visited
            if curr == len(word):
                return True
            if min(i, j) < 0 or i >= rows or j >= cols or (i, j) in visited or board[i][j] != word[curr] or curr >= len(word):
                return False
            visited.add((i, j))
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            found = False
            for dr, dc in directions:
                if dfs(i+dr, j+dc, curr+1):
                    found = True
                    break
            visited.remove((i, j))
            return found
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False



