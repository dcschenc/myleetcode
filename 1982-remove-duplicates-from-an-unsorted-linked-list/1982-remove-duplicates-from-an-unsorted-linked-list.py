# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1836.Remove%20Duplicates%20From%20an%20Unsorted%20Linked%20List
        cnt = Counter()
        cur = head
        while cur:
            cnt[cur.val] += 1
            cur = cur.next
        dummy = ListNode(0, head)
        pre, cur = dummy, head
        while cur:
            if cnt[cur.val] > 1:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return dummy.next