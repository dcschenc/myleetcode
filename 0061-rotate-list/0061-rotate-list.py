# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/0000-0099/0061.Rotate%20List
        if head is None or head.next is None:
            return head
        cur, n = head, 0
        while cur:
            n += 1
            cur = cur.next
        k %= n
        if k == 0:
            return head
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast, slow = fast.next, slow.next

        ans = slow.next
        slow.next = None
        fast.next = head
        return ans

        # if head is None:
        #     return None
            
        # node = head
        # count = 1
        # while node.next:
        #     count += 1
        #     node = node.next
        # # node.next = head
        # last_node = node
        # node = head
        # k = count - k % count
        # while k > 1:
        #     node = node.next
        #     k -= 1
        # last_node.next = head
        # head = node.next
        # node.next = None
        # return head