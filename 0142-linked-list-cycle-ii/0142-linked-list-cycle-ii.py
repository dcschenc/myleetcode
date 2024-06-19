# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/0100-0199/0142.Linked%20List%20Cycle%20II
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next            
            fast = fast.next.next
            if slow == fast:
                slow = head
                while fast is not None:
                    if slow == fast:
                        return slow
                    slow = slow.next
                    fast = fast.next
                         
        return None