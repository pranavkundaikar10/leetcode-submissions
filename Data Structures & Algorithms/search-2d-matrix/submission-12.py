class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            mid = l + (r-l) //2
            # if  not (matrix[l][0] <= target <= matrix[r][len(matrix[0])-1]):
            #     return False
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][len(matrix[0])-1]:
                l = mid + 1
            else:
                i, j = 0, len(matrix[0])-1
                while i <= j:
                    rmid = (i + j) // 2
                    if matrix[mid][rmid] < target:
                        i = rmid + 1
                    elif matrix[mid][rmid] > target:
                        j = rmid - 1
                    else:
                        return True
                return False
        return False
            
            
