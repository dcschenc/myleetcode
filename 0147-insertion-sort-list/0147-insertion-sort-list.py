# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

        return dummy.next
        
        def insert_node(node):
            cur = dummy.next
            prev = dummy            
            while cur:
                if cur.val >= node.val:
                    prev.next = node
                    node.next = cur
                    return
                prev = cur
                cur = cur.next
            prev.next = node
            node.next = None

        dummy = ListNode(-1)
        node = head
        while node:            
            tmp = node.next
            insert_node(node)
            node = tmp
        
        return dummy.next