# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            total, cnt = node.val, 1
            if not node.left and not node.right:
                ans[0] += 1
                return node.val, 1
            else:
                if node.left:
                    left_total, left_cnt = dfs(node.left)
                    total += left_total
                    cnt += left_cnt
                if node.right:
                    right_total, right_cnt = dfs(node.right)
                    total += right_total
                    cnt += right_cnt
            if total // cnt == node.val:
                ans[0] += 1
            return total, cnt
        
        ans = [0]
        dfs(root)
        return ans[0]

        

