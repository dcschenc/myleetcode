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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1367.Linked%20List%20in%20Binary%20Tree
        def dfs(head, root):
            if head is None:
                return True
            if root is None or root.val != head.val:
                return False
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        if root is None:
            return False
        return (
            dfs(head, root)
            or self.isSubPath(head, root.left)
            or self.isSubPath(head, root.right)
        )
        
        def isMatch(node, linked_list_node):
            if not linked_list_node:
                return True
            if not node:
                return False
            return node.val == linked_list_node.val and (isMatch(node.left, linked_list_node.next) or isMatch(node.right, linked_list_node.next))

        def dfs(node):
            if not node:
                return False
            return isMatch(node, head) or dfs(node.left) or dfs(node.right)

        return dfs(root)
        
    #     if not head:
    #         return True       
    #     if not root:
    #         return False
    #     if root.val == head.val:
    #         # If there's a match, check the rest of the linked list
    #         if self.matchRemaining(head.next, root.left) or self.matchRemaining(head.next, root.right):
    #             return True
            
    #     # Continue searching in the subtrees
    #     return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    # def matchRemaining(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    #     # Check if the remaining linked list matches the path in the binary tree
    #     if not head:
    #         return True
    #     if not root:
    #         return False
    #     if root.val == head.val:
    #         return self.matchRemaining(head.next, root.left) or self.matchRemaining(head.next, root.right)
    #     return False
           