# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
            
        node = head
        count = 1
        while node.next:
            count += 1
            node = node.next
        # node.next = head
        last_node = node
        node = head
        k = count - k % count
        while k > 1:
            node = node.next
            k -= 1
        last_node.next = head
        head = node.next
        node.next = None
        return head