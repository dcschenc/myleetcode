# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter()
        while head:
            counter[head.val] += 1
            head = head.next
        head = ListNode()
        node = head
        for v in counter.values():
            node.next = ListNode(v)
            node = node.next
        return head.next