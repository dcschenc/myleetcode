# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2487.Remove%20Nodes%20From%20Linked%20List
        stack = []
        node = head
        stack = [node]
        while stack and node.next:
            while stack and stack[-1].val < node.next.val:
                stack.pop()
            node = node.next
            stack.append(node)      

        prev = None
        while stack:
            cur = stack.pop()
            cur.next = prev
            prev = cur
        return prev
