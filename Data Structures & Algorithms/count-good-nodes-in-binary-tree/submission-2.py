# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        queue = deque([(root, float("-inf"))])
        while queue:
            for i in range(len(queue)):
                node, prevMax = queue.popleft()
                if node.val >= prevMax:
                    res += 1
                if node.left: queue.append((node.left, max(node.val, prevMax)))
                if node.right: queue.append((node.right, max(node.val, prevMax)))
        return res



        