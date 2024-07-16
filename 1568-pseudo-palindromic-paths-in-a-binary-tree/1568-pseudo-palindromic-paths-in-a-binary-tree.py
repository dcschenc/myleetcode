# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1457.Pseudo-Palindromic%20Paths%20in%20a%20Binary%20Tree
        def dfs(root: Optional[TreeNode], mask: int):
            if root is None:
                return 0
            mask ^= 1 << root.val
            if root.left is None and root.right is None:
                return int((mask & (mask - 1)) == 0)
            return dfs(root.left, mask) + dfs(root.right, mask)

        return dfs(root, 0)


        # def is_palindrome():
        #     total, odd = 0, 0
        #     for i in range(1, 10):
        #         total += counter[i]
        #         if counter[i] % 2 == 1:
        #             odd += 1           
        #     if odd > 2 or total % 2 == 1 and odd == 0 or total % 2 == 0 and odd > 0:
        #         return False
        #     return True

        # def dfs(node):
        #     if not node.left and not node.right:
        #         counter[node.val] += 1
        #         if is_palindrome():
        #             ans[0] += 1
        #         counter[node.val] -= 1
        #         return
            
        #     counter[node.val] += 1
        #     if node.left:
        #         dfs(node.left)
        #     if node.right:
        #         dfs(node.right)
        #     counter[node.val] -= 1
        
        # ans, counter = [0], defaultdict(int)
        # dfs(root)
        # return ans[0]
        