# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = [None] * k        
        node = head
        n = 0
        while node:
            n += 1
            node = node.next       
        size = n//k
        remainder = n%k
        node = head
        prev = None
        for i in range(remainder):
            res[i] = node
            prev = node
            for j in range(size+1):
                prev = node
                node = node.next
            prev.next = None
            
        for i in range(remainder, k):
            res[i] = node
            prev = node
            for j in range(size):
                prev = node
                node = node.next
            if prev:
                prev.next = None
            
        return res
                    

