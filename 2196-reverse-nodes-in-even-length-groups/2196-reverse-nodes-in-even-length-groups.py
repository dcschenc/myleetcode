# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2074.Reverse%20Nodes%20in%20Even%20Length%20Groups
        def reverse_linklist(cur, cnt):
            dummy = ListNode(-1, cur)
            prev = None
            while cnt > 0 and cur:                             
                tmp = cur.next
                cur.next = prev                
                prev = cur        
                cur = tmp
                cnt -= 1
            return prev, dummy.next, cur

        node = head
        n = 0
        while node:
            n += 1
            node = node.next

        cnt = 1
        node = head
        last_node = None
        while node:
            if cnt % 2 == 0:
                start, end, node = reverse_linklist(node, cnt)
                end.next = node
                # print(start, end, node)
                last_node.next = start
                last_node = end  
            else:
                for i in range(cnt):
                    prev = node
                    node = node.next
                last_node = prev
            n -= cnt
            cnt += 1
            cnt = min(cnt, n)
        return head