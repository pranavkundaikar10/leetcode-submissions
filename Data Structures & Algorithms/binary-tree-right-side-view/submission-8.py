# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            val = None
            for i in range(len(queue)):
                node = queue.popleft()                
                if not node:
                    continue
                val = node.val
                queue.append(node.left)
                queue.append(node.right)
            
            if val:
                res.append(val)

        
        return res