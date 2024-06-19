# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """        
        ######  split #######
        node = head
        slow, fast = node, node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None  # list 1 end
        
        ####### reverse the 2nd part #########
        prev, node = head2, head2
        while node:
            tmp = node.next
            node.next = prev           
            prev = node
            node = tmp
        if head2:
            head2.next = None  # list 2 end
        
        ######### construct ##########
        node1 = head
        node2 = prev
        while node1 and node2:
            tmp1 = node1.next
            tmp2 = node2.next
            node1.next = node2
            node2.next = tmp1
            node1 = tmp1
            node2 = tmp2
    
        

        