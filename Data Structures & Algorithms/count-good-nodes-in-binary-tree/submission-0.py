# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(root, maxVal):
            if not root:
                return 0
            good = 0
            print(root.val, maxVal)
            if root.val >= maxVal:
                print('add to count')
                good += 1
            maxVal = max(root.val, maxVal)
            return good + dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, float('-inf'))
            
        