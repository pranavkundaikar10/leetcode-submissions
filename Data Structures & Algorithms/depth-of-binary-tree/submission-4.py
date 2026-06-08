# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return res
        q = deque([root])
        while q:
            print(q)
            qLen = len(q)
            l = 0
            for i in range(qLen):
                node = q.popleft()
                if not node:
                    continue
                l = 1
                q.append(node.left)
                q.append(node.right)
            res += l
        return res