"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1666.Change%20the%20Root%20of%20a%20Binary%20Tree
        def dfs(cur, prev):
            if not cur.parent:
                cur.parent = prev
                return
            if cur.left:
                cur.right = cur.left
            cur.left = cur.parent
            parent = cur.parent
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None            
            dfs(cur.parent, cur)
            cur.parent = prev

        dfs(leaf, None)
        return leaf
        