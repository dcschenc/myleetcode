# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def calculate_depth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        # Main function starts here
        # If the root is None, the tree is empty and has no nodes
        if root is None:
            return 0

        # Calculate the depth of the left and right subtrees
        left_depth = calculate_depth(root.left)
        right_depth = calculate_depth(root.right)

        # If the left and right subtrees have the same depth, it means the left subtree is complete
        # We can directly calculate the nodes in the left subtree using the formula (2^depth) - 1
        # and then recursively count the nodes in the right subtree.
        if left_depth == right_depth:
            # Left shift operation (1 << left_depth) calculates 2^left_depth
            # Add the count of nodes in the right subtree.
            return (1 << left_depth) + self.countNodes(root.right)
      
        # If the left and right subtree depths differ, the right subtree is complete
        # We calculate the nodes for the right subtree using the formula (2^depth) - 1
        # and recursively count the nodes in the left subtree.
        else:
            # Add the count of nodes in the left subtree.
            return (1 << right_depth) + self.countNodes(root.left)

        # Height = H = log(n) where n = total number of nodes
        # Time: O(H * H) = O(log(n)^2) = O(Log^2 n)
        # Auxiliary Space: O(H) = O(log(n))
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root: 
            return 0
        
        leftHeight = getLeftHeight(root)
        rightHeight = getRightHeight(root)
        
        if leftHeight == rightHeight: 
            return 2 ** leftHeight - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)              
    