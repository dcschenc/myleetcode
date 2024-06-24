# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0437.Path%20Sum%20III
        def dfs(node, s):
            if node is None:
                return 0
            s += node.val
            ans = cnt[s - targetSum]
            cnt[s] += 1
            ans += dfs(node.left, s)
            ans += dfs(node.right, s)
            cnt[s] -= 1
            return ans

        cnt = Counter({0: 1})
        return dfs(root, 0)

        # def count_num(path):
        #     cur = 0
        #     cnt = 0
        #     for val in path[::-1]:
        #         cur += val
        #         if cur == targetSum:
        #             cnt += 1
        #     return cnt

        # def dfs(node, path):
        #     nonlocal res
        #     if not node:
        #         return            
        #     path.append(node.val)            
        #     res += count_num(path)
        #     dfs(node.left, path)
        #     dfs(node.right, path)
        #     path.pop()

        # res = 0
        # dfs(root, [])
        # return res