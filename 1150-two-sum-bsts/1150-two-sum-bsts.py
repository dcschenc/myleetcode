# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(root: Optional[TreeNode], i: int):
            if root is None:
                return
            dfs(root.left, i)
            nums[i].append(root.val)
            dfs(root.right, i)

        nums = [[], []]
        dfs(root1, 0)
        dfs(root2, 1)
        i, j = 0, len(nums[1]) - 1
        while i < len(nums[0]) and ~j:
            x = nums[0][i] + nums[1][j]
            if x == target:
                return True
            if x < target:
                i += 1
            else:
                j -= 1
        return False
        
        def dfs_1(node):
            if not node:
                return
            hm.add(target - node.val)            
            dfs_1(node.left)
            dfs_1(node.right)

        def dfs_2(node):
            if not node:
                return False
            if node.val in hm:
                return True
            ans = False
            ans |= dfs_2(node.left)
            ans |= dfs_2(node.right)
            return ans

        hm = set()
        dfs_1(root1)
        return dfs_2(root2)
