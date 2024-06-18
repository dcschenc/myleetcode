# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # #### recursive
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None:
    #         return None
    #     if head.next is None:
    #         return head
    #     first, second, rest = head, head.next, self.swapPairs(head.next.next)
    #     second.next, first.next = first, rest
    #     return second

    ### non recursive
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        node = dummy
        while node.next and node.next.next:
            node1 = node.next
            node2 = node.next.next

            tmp = node2.next
            node2.next = node1
            node1.next = tmp
            node.next = node2
            node = node1
        return dummy.next
