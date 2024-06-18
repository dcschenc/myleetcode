# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  
        if not head or left == right:
            return head
        # Dummy node to simplify code
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        # Move to the position before the reversal
        for _ in range(left - 1):
            pre = pre.next
        p, q = pre, pre.next
        # Reverse the portion of the linked list between m and n
        cur = q
        prev = None
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        # Connect the reversed portion back to the original list
        q.next = cur
        p.next = prev

        return dummy.next
