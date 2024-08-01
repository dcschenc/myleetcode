# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        cur = head.next
        s = 0
        while cur:
            if cur.val != 0:
                s += cur.val
            else:
                node.next = ListNode(s)
                node = node.next
                s = 0
            cur = cur.next
        return dummy.next

        dummy = ListNode(-1)
        prev = None
        node = head
        while node:
            if node.val == 0:                      
                if prev:          
                    prev.next = node
                if node.next:
                    prev = node
                else:
                    prev.next = None
            else:
                prev.val += node.val
            node = node.next       
        return head

        # dummy = ListNode(-1)
        # cur = dummy
        # node = head.next
        # val = 0
        # while node:
        #     if node.val == 0:
        #         cur.next = ListNode(val)
        #         cur = cur.next
        #         val = 0
        #     else:
        #         val += node.val
        #     node = node.next
        # return dummy.next
