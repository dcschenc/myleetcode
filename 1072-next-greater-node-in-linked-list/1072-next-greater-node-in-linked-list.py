# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        res = [0] * count       
        node = head 
        idx = 0
        stack.append((node.val, 0))
        node = node.next
        while node:
            while stack and node.val > stack[-1][0]:
                res[stack[-1][1]] = node.val
                stack.pop()            
            idx += 1
            stack.append((node.val, idx))
            node = node.next        
        return res

