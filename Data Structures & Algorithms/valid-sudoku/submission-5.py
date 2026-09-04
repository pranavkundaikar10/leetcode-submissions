class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        rset, cset, bset = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if val in rset[r] or val in cset[c] or val in bset[(r//3,c//3)]:
                    return False
                rset[r].add(val)
                cset[c].add(val)
                bset[(r//3, c//3)].add(val)
        return True