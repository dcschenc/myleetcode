# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = dmy_left = ListNode(-1)
        right = dmy_right = ListNode(-1)
        node = head
        while node:
            if x <= node.val:
                right.next = node
                right = right.next
            else:
                left.next = node
                left = left.next
            node = node.next
        right.next = None
        if dmy_right.next:
            left.next = dmy_right.next
        
        head = dmy_left.next
        return head

                