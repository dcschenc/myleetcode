# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # if not nums: return None
        # stack = []
        # for num in nums:
        #     node = TreeNode(num)
        #     while stack and stack[-1].val < num:
        #         node.left = stack.pop()
        #     if stack:
        #         stack[-1].right = node
        #     stack.append(node)

        # return stack[0]

        def dfs(nums):
            if len(nums) == 0:
                return None
            max_val = max(nums)
            idx = nums.index(max_val)
            node = TreeNode(max_val)
            node.left = dfs(nums[:idx])
            node.right = dfs(nums[idx+1:])
            return node
        return dfs(nums)
