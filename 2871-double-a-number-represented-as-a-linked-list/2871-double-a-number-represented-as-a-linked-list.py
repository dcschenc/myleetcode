# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            dummy = ListNode()
            cur = head
            while cur:
                next = cur.next
                cur.next = dummy.next
                dummy.next = cur
                cur = next
            return dummy.next

        head = reverse(head)
        dummy = cur = ListNode()
        mul, carry = 2, 0
        while head:
            x = head.val * mul + carry
            carry = x // 10
            cur.next = ListNode(x % 10)
            cur = cur.next
            head = head.next
        if carry:
            cur.next = ListNode(carry)
        return reverse(dummy.next)
        
        sys.set_int_max_str_digits(100000)
        node = head
        total = 0
        while node:
            total = total * 10 + node.val
            node = node.next
        node = dummy = ListNode()
        total *= 2
        for d in str(total):
            cur = ListNode(d)
            node.next = cur
            node = node.next
        return dummy.next