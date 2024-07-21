# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:   
        def dfs(node, leaves):
            # leaves = set()            
            if not node.left and not node.right:
                # leaves.add(node.val)
                leaves[node.val] += 1
            else:            
                if node.left:
                    dfs(node.left, leaves)
                if node.right:
                    dfs(node.right, leaves)
            return leaves

        leaves1 = defaultdict(int)
        leaves2 = defaultdict(int)

        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
            
