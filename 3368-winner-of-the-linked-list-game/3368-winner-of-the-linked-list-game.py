# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        even_cnt = odd_cnt = 0
        while head:
            even = head.val
            head = head.next
            odd = head.val
            head = head.next
            if even > odd:
                even_cnt += 1
            elif even < odd:
                odd_cnt += 1
        if even_cnt > odd_cnt:
            return 'Even' 
        elif even_cnt < odd_cnt:
            return 'Odd'
        else:
            return 'Tie'
            


        