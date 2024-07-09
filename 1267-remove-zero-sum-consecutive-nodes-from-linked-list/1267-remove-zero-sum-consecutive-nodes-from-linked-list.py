# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1171.Remove%20Zero%20Sum%20Consecutive%20Nodes%20from%20Linked%20List
        dummy = ListNode(next=head)
        last = {}
        s, cur = 0, dummy
        while cur:
            s += cur.val
            last[s] = cur
            cur = cur.next
            
        s, cur = 0, dummy
        while cur:
            s += cur.val
            cur.next = last[s].next
            cur = cur.next
        return dummy.next


        # dummy = ListNode(0)
        # dummy.next = head

        # prefix_sum = 0
        # prefix_sum_map = {0: dummy}

        # current = dummy.next

        # while current:
        #     prefix_sum += current.val

        #     if prefix_sum in prefix_sum_map:
        #         # Remove nodes between the previous and current node (inclusive)
        #         prev = prefix_sum_map[prefix_sum]
        #         prev.next = current.next

        #         # Update the prefix sum map to reflect the removal
        #         node = prev.next
        #         temp_sum = prefix_sum + node.val
        #         while temp_sum != prefix_sum:
        #             del prefix_sum_map[temp_sum]
        #             node = node.next
        #             temp_sum += node.val
        #     else:
        #         prefix_sum_map[prefix_sum] = current

        #     current = current.next

        # return dummy.next

        # def get_sum_zero(node):            
        #     hm = {0: None}
        #     prefix_sum = 0
        #     while node:            
        #         prefix_sum = prefix_sum + node.val
        #         if prefix_sum in hm:
        #             pre = hm.get(prefix_sum)
        #             return pre, node
        #         else:
        #             hm[prefix_sum] = node
        #         node = node.next    
        #     return None, None        

        # node = head
        # while True:
        #     pre, cur = get_sum_zero(node)
        #     if not pre and not cur:
        #         break
        #     if pre == None:
        #         node = cur.next
        #         head = node
        #     else:
        #         pre.next = cur.next
        # return head
        
            