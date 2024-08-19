# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        node = dummy.next
        nums = set(nums)
        while node:
            if node.val not in nums:
                prev = node
            else:
                prev.next = node.next
            node = node.next
        return dummy.next