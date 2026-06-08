# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = collections.deque()
        q.append(root)
        while q:
            qLen = len(q)
            right = None
            for i in range(qLen):
                node = q.popleft()
                if not node:
                    continue
                right = node.val
                q.append(node.left)
                q.append(node.right)
            if right:
                res.append(right)

        return res

        