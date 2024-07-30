# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2130.Maximum%20Twin%20Sum%20of%20a%20Linked%20List
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            #### reverse the first part #####
            slow.next, prev, slow = prev, slow, slow.next

        maxi = -maxsize
        while slow:
            maxi = max(maxi, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return maxi

        # cnt = 0
        # node = head
        # val_list = []
        # while node:
        #     cnt += 1
        #     val_list.append(node.val)
        #     node = node.next
        # max_s = 0
        # for i in range(cnt//2):
        #     s = val_list[i] + val_list[cnt-i-1]
        #     if s > max_s:
        #         max_s = s
        # return max_s
