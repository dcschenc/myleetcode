# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = head
        while pre:
            for _ in range(m - 1):
                if pre:
                    pre = pre.next
            if pre is None:
                return head
            cur = pre
            for _ in range(n):
                if cur:
                    cur = cur.next
            pre.next = None if cur is None else cur.next
            pre = pre.next
        return head
        
        node = head
        while node.next:
            for _ in range(m-1):
                node = node.next
                if not node:
                    break
            if not node:
                break
            prev = node
            for _ in range(n+1):
                node = node.next
                if not node:
                    break
            prev.next = node if node else None
            if node:
                prev.next = node
            else:
                prev.next = None
                break
        return head