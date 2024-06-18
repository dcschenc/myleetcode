# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_tree(left, right):
            if left > right:
                return None
            mid = (left+right)//2
            node = TreeNode(sorted_list[mid])
            node.left =  get_tree(left, mid-1)
            node.right = get_tree(mid+1, right )
            return node
            
        sorted_list = []
        node = head
        while node:
            sorted_list.append(node.val)
            node = node.next            
        n = len(sorted_list) - 1
        return get_tree(0, n)

        # def getLength(head: ListNode) -> int:
        #     length = 0
        #     while head:
        #         length += 1
        #         head = head.next
        #     return length

        # def buildBST(start: int, end: int) -> TreeNode:
        #     nonlocal head

        #     if start > end:
        #         return None

        #     mid = (start + end) // 2
        #     left = buildBST(start, mid - 1)
        #     root = TreeNode(head.val)
        #     head = head.next
        #     right = buildBST(mid + 1, end)
        #     root.left = left
        #     root.right = right
        #     return root

        # length = getLength(head)
        # return buildBST(0, length - 1)

        # def get_mid(node):
        #     left, right = head, head
        #     while right.next and right.next.next:
        #         left = left.next
        #         right = right.next.next
        #     return left
        # mid = get_mid(head)
        # root = TreeNode(mid.val)
        # root.left = self.sortedListToBST(head) 
        # root.right = self.sortedListToBST(mid.next)
        # return root