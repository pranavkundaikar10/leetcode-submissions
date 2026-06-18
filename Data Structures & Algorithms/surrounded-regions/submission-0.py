class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        edge = set()
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        def backtrack(i, j, subset, visited):
            
            if i < 0 or j < 0 or i >= rows or j >= cols or (i,j) in edge:
                return False
            
            if (i, j) in visited:
                return True

            if board[i][j] == 'X':
                return True
            if board[i][j] == 'O':
                subset.append((i, j))
            visited.add((i, j))
            for dr, dc in directions:
                if not backtrack(i+dr, j+dc, subset, visited):
                    return False
            return True

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in edge and board[i][j] == 'O':
                    subset = []
                    if backtrack(i, j, subset, set()):
                        for r, c in subset:
                            board[i][j] = 'X'
                    else:
                        edge.update(subset)
