# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.val, fast)
        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr_l1, curr_l2 = head, prev
        while curr_l2:
            tmp_l1 = curr_l1.next
            tmp_l2 = curr_l2.next
            curr_l1.next = curr_l2
            curr_l2.next = tmp_l1
            curr_l1 = tmp_l1
            curr_l2 = tmp_l2
        