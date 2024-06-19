# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        # Array containing all the nodes in the sorted order
        self.nodes_sorted = []

        # Pointer to the next smallest element in the BST
        self.index = -1

        # Call to flatten the input binary search tree
        self._inorder(root)

    def _inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self._inorder(root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(root.right)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)

# class BSTIterator:
#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         self.push_stack(root)        

#     def next(self) -> int:
#         res = self.stack[-1]
#         self.stack.pop()
#         if res.right:
#             self.push_stack(res.right)
#         return res.val        

#     def hasNext(self) -> bool:
#         return len(self.stack) > 0
    
#     def push_stack(self, node):      
#         while node:
#             self.stack.append(node)
#             node = node.left          

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()