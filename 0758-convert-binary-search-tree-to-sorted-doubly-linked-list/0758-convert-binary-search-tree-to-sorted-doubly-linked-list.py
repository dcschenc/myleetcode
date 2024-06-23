"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':        
        def dfs(node):
            nonlocal previous, head
            # Base case: if the node is None, return to the previous call.
            if node is None:
                return None        
            # Recursive case: traverse the left subtree.
            dfs(node.left)                               
            if previous:
                # Link the previous node with the current node from the left.
                previous.right = node
                # Link the current node with the previous node from the right.
                node.left = previous
            else:
                # If this node is the leftmost node, it will be the head of the doubly linked list.
                head = node
            # Mark the current node as the previous one before the next call.
            previous = node          
            # Recursive case: traverse the right subtree.
            dfs(node.right)

        # If the input tree is empty, return None.
        if root is None:
            return None

        # Initialize the head and previous pointer used during the in-order traversal.
        head = previous = None
        # Perform the in-order traversal to transform the tree to a doubly linked list.
        dfs(root)
        # Connect the last node visited (previous) with the head of the list to make it circular.
        previous.right = head
        head.left = previous
        return head


        # def dfs(cur, prev):            

        #     if :
        #         return node

        #     if prev is not None:
        #         prev.right = cur
        #         cur.left = prev
        #     else:
        #         head = cur
        #     cur.right = prev

        #     if cur.left:
        #         cur.left = dfs(cur.left, cur)            
        #     if cur.right:                
        #         return dfs(cur.right, prev)
        #     return prev
        
        # head = None
        # # dummy.right = root
        # prev = dfs(root, None)
        # prev.left = head
        # head.right = prev
        # return head