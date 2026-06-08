# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0
            leftstatus, leftdepth = dfs(root.left)
            rightstatus, rightdepth = dfs(root.right)
            if not leftstatus or not rightstatus or abs(leftdepth - rightdepth) > 1:
                return False, max(leftdepth, rightdepth)
            return True, 1 + max(leftdepth, rightdepth)
        status, depth = dfs(root)
        return status
        