# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-101, head)
        node = dummy_node.next
        prev = dummy_node
        while node and node.next:
            if node.next.val != node.val:
                prev = node
                node = node.next
            else:
                while node.next and node.next.val == node.val:
                    node = node.next
                node = node.next
                prev.next = node

        return dummy_node.next
