class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board[0]), len(board[1])
        rsets, csets, bsets = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rsets[r] or val in csets[c] or val in bsets[(r//3, c//3)]:
                    return False
                rsets[r].add(val)
                csets[c].add(val)
                bsets[(r//3, c//3)].add(val)
        return True


