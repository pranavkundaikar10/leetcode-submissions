# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        while n and curr:
            curr = curr.next
            n -= 1
        prev = dummy
        while curr:
            prev = prev.next
            curr = curr.next
        
        prev.next = prev.next.next
        return dummy.next
