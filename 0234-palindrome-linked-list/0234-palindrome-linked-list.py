# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Function to reverse a linked list
        def reverse_list(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev

        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = reverse_list(slow)

        # Compare the original first half with the reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True
    
        # fast, slow = head, head
        # while fast.next and fast.next.next:           
        #     fast = fast.next.next
        #     slow = slow.next
        
        # if fast.next is None:
        #     fast = ListNode(slow.val)
        #     fast.next = slow.next
        # else:
        #     fast = slow.next
        # slow.next = None
            
        # prev, curr = head, head
        # while curr:            
        #     tmp = curr.next
        #     curr.next = prev
        #     if prev == head:
        #         prev.next = None
        #     prev = curr            
        #     curr = tmp
            
        # while prev and fast:
        #     if prev.val != fast.val:
        #         return False
        #     prev = prev.next
        #     fast = fast.next
        # return True
            
        
            
        
        