# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        if not root:
            return diameter
        root_depth = self.depth(root.left) + self.depth(root.right)
        return max(root_depth, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))

    def depth(self, root):
        if not root:
            return 0        
        return 1 + max(self.depth(root.left), self.depth(root.right))
        