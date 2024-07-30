# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2095.Delete%20the%20Middle%20Node%20of%20a%20Linked%20List
        dummy = ListNode(next=head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy.next
        # Initialize two pointers, slow and fast, both initially pointing to the head
        slow = fast = head
        prev = None  # To keep track of the node before the slow pointer

        # Move the fast pointer two steps at a time and the slow pointer one step at a time
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # After the loop, slow points to the middle node
        # Delete the middle node by updating the pointers of the previous node
        if prev:
            prev.next = slow.next
        else:
            # If there is no previous node, it means the head itself is the middle node
            # Update the head to skip the middle node
            head = head.next

        return head