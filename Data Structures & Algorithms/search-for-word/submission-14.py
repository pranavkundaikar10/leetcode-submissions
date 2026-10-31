class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i, visited):
            if i >= len(word):
                return True

            if min(r,c) < 0 or r >= rows or c >= cols or board[r][c] != word[i] or (r, c) in visited: 
                return False
            i += 1
            visited.add((r,c))
            status = (
                dfs(r-1,c, i, visited) or
                dfs(r+1,c, i, visited) or
                dfs(r,c-1, i, visited) or
                dfs(r,c+1, i, visited)
                )
            visited.remove((r,c))
            return status

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True
        return False