class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(i, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            matrix[i].reverse()



        