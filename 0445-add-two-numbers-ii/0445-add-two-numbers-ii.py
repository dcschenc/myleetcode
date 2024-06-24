# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(0)
        carry = 0
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            val = val1 + val2 + carry
            node = ListNode(val % 10)
            node.next = dummy.next
            dummy.next = node
            carry = val // 10       
        return dummy.next

        # len_1 = 0
        # len_2 = 0
        # dummy_1 = ListNode(0, l1)
        # dummy_2 = ListNode(0, l2)
        # while l1:
        #     len_1 += 1
        #     l1 = l1.next
        # while l2:
        #     len_2 += 1
        #     l2 = l2.next
        # if len_1 < len_2:
        #     dummy_1, dummy_2 = dummy_2, dummy_1
        # dummy = ListNode(0, dummy_1.next)
        # node = dummy.next
        # for i in range(len_1 - len_2):
        #     node = node.next
        # node2 = dummy_2.next
        # for i in range(len_2):
        #     node.val = node.val + node2.val
        #     node = node.next
        #     node2 = node2.next
        # return dummy.next

