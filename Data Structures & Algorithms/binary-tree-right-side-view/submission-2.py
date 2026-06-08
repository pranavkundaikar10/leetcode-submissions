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
        q = deque([root])
        while q:
            lenq = len(q)
            status = False
            for i in range(lenq):
                node = q.popleft()
                if not node:
                    continue
                if not status:
                    res.append(node.val)
                    status = True
                q.append(node.right)
                q.append(node.left)
        return res
