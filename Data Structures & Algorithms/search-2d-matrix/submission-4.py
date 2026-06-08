class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        while top <= bottom:
            # m = (bottom - top + 1)//2
            m = top + (bottom-top)//2
            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            # elif target > matrix[m][-1]
            else:
                l, r = 0, len(matrix[m])-1
                while l <= r:
                    mid = l + (r - l)//2
                    if matrix[m][mid] < target:
                        l = mid + 1
                    elif matrix[m][mid] > target:
                        r = mid - 1
                    else:
                        print('found', m, mid)
                        return True
                return False
        return False

                


        