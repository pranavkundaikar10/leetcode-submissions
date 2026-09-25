class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(i, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in range(rows):
            matrix[row].reverse()


            