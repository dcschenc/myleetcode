# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        d_odd, d_even = ListNode(0), ListNode(0)
        odd = d_odd
        even = d_even
        count = 1
        cur = head
        while cur:
            if count%2 == 1:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            count += 1
        even.next = None
        odd.next = d_even.next
        return d_odd.next