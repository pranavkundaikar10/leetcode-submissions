# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            curr = prevGroup
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next
            
            nextGroup = curr.next
            groupStart = prevGroup.next
            prev = nextGroup
            curr = prevGroup.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            prevGroup.next = prev
            prevGroup = groupStart



