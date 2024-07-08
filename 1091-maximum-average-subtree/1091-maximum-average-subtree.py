# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1120.Maximum%20Average%20Subtree
        def dfs(root):
            if root is None:
                return 0, 0
            ls, ln = dfs(root.left)
            rs, rn = dfs(root.right)
            s = root.val + ls + rs
            n = 1 + ln + rn
            nonlocal ans
            ans = max(ans, s / n)
            return s, n

        ans = 0
        dfs(root)
        return ans


        def dfs(node):
            total = node.val
            cnt = 1
            if not node.left and not node.right:
                cnt = 1
            else:            
                if node.left:
                    left_total, left_cnt = dfs(node.left)
                    total += left_total
                    cnt += left_cnt
                if node.right:
                    right_total, right_cnt = dfs(node.right)
                    total += right_total
                    cnt += right_cnt
            
            ans[0] = max(ans[0], total / cnt)

            return total, cnt

        ans = [-1]
        dfs(root)
        return ans[0]