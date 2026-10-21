class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        res = [[0]*rows for _ in range(cols)]
        print(res)

        for r in range(rows):
            for c in range(cols):
                print(r, c)
                res[c][r] = matrix[r][c]

        return res


        