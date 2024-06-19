# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val == val:                
                prev.next = cur.next  
            else:
                prev = cur            
            cur = cur.next
        return dummy.next

        # prev, curr = head, head
        # while curr:
        #     if curr.val == val:                
        #         prev.next = curr.next  
        #         if curr == head:
        #             head = curr.next
        #         # curr = curr.next
        #     else:
        #         prev = curr            
        #         # curr = curr.next
        #     curr = curr.next
        # return head