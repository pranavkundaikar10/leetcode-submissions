class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, j, curr):
            nonlocal visited
            if curr == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j >= cols or curr >= len(word) or (i, j) in visited or word[curr] != board[i][j]:
                return False
            
            dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited.add((i, j))
            found = False
            for d in dr:
                if dfs(i+d[0], j+d[1], curr + 1):
                    found = True
                    break
            visited.remove((i, j))
            return found



        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
            



        