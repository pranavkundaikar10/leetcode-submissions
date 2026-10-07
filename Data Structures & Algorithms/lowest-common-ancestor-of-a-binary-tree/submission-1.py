# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        def dfs(root):
            nonlocal lca
            if not root:
                return [False, False]
            if lca:
                return [False, False]
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = [
                left[0] or right[0] or (root == p),
                left[1] or right[1] or (root == q)
            ]
            if res[0] and res[1] and not lca:
                lca = root
            return res

        dfs(root)
        return lca        