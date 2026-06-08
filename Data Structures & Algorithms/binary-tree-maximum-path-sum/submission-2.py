# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val
        def dfs(root):
            nonlocal res
            if not root:
                return 0

            lmax = max(dfs(root.left), 0)
            rmax = max(dfs(root.right), 0)
            print('root.val', root.val, lmax, rmax)            
            # res = max(lmax, rmax, 0)
            res = max(res, root.val + lmax + rmax)
            print('final res', res)
            print('return', root.val + max(lmax, rmax))
            return root.val+max(lmax, rmax)
        dfs(root)
        return res
        