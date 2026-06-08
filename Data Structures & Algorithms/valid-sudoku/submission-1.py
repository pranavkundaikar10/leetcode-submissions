class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        rset, cset, gset = defaultdict(set), defaultdict(set),defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                val = board[r][c]
                if val in rset[r] or val in cset[c] or val in gset[(r//3, c//3)]:
                    return False
                rset[r].add(val)
                cset[c].add(val)
                gset[(r//3, c//3)].add(val)
        return True

        