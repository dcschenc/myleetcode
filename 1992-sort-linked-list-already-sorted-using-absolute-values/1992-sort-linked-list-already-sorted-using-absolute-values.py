# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = head, head.next
        while cur:
            if cur.val < 0:
                t = cur.next
                prev.next = t
                cur.next = head
                head = cur
                cur = t
            else:
                prev, cur = cur, cur.next
        return head