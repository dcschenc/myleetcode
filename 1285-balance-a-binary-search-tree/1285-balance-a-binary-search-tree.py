# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1382.Balance%20a%20Binary%20Search%20Tree
        def dfs(node):
            if not node:
                return
            nodes.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        def construct_bst(start, end):
            if start == end:
                return None
            mid = (start + end) // 2
            node = TreeNode(nodes[mid])
            node.left = construct_bst(start, mid)
            node.right = construct_bst(mid + 1, end)
            return node

        nodes = []
        dfs(root)
        nodes.sort()
        n = len(nodes)
        return construct_bst(0, n)

        