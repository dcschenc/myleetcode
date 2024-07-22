# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II
        def dfs(node):
            if node is None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                ans[0] = node
            if (left or right) and (node.val == p.val or node.val == q.val):
                ans[0] = node
            return left or right or node.val == p.val or node.val == q.val

        ans = [None]
        dfs(root)
        return ans[0]
        
        # def dfs_check(node):
        #     if not node:
        #         return 
        #     if node == p or node == q:
        #         ans.append(node)
        #     if node.left:
        #         dfs_check(node.left)
        #     if node.right:
        #         dfs_check(node.right)

        # def dfs(node):
        #     if node is None or node == p or node == q:
        #         return node
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if left and right:
        #         return node
        #     if left:
        #         return left                
        #     elif right:
        #         return right               
        #     else:
        #         return None
        # ans = []
        # dfs_check(root)
        # if len(ans) < 2:
        #     return None
        # return dfs(root)
        