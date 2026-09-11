# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        carry = 0
        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            n = ListNode()
            n.val = s if s < 10 else s % 10
            carry = 0 if s < 10 else 1
            print(n.val)
            curr.next = n
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # if l1:
        #     curr.next = l1
        # if l2:
        #     curr.next = l2
        if carry:
            curr.next = ListNode(carry)
        
        return l3.next

        
        