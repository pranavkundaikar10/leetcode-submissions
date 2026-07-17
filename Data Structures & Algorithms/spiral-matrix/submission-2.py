class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        res = []
        while top <= bottom and left <= right:
            for col in range(left, right+1):
                res.append(matrix[top][col])
            top +=1
            for row in range(top, bottom+1):
                res.append(matrix[row][right])
            right -=1
            if not (top<=bottom and left <= right):
                return res
            for col in range(right, left-1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
            for row in range(bottom, top-1, -1):
                res.append(matrix[row][left])
            left += 1

        return res


