class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def backtrack(i, j, curr):
            if curr == len(word):
                return True

            if min(i, j) < 0 or i >= rows or j >= cols or board[i][j] != word[curr] or (i, j) in visited:
                return False
            found = False
            visited.add((i, j))
            for dr, dc in directions:
                if backtrack(i+dr, j+dc, curr+1):
                    found = True
                    break
            visited.remove((i, j))
            return found


        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False