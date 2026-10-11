# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        status = True
        def dfs(root):
            nonlocal status
            if not root:
                return 0

            if not status:
                return 0

            l, r = dfs(root.left), dfs(root.right)

            if abs(l - r) > 1:
                status = False
            return 1 + max(l, r)
        dfs(root)
        return status
