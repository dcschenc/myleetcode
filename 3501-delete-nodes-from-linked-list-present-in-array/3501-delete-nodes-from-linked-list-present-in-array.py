# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3217.Delete%20Nodes%20From%20Linked%20List%20Present%20in%20Array
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