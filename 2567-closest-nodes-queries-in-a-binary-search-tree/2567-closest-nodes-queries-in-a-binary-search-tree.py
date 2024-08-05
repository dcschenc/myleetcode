# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2476.Closest%20Nodes%20Queries%20in%20a%20Binary%20Search%20Tree
        def dfs(node: Optional[TreeNode]):
            if node is None: 
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)

        nums = []
        dfs(root)
        ans = []
        for x in queries:
            i = bisect_left(nums, x + 1) - 1
            j = bisect_left(nums, x)
            mi = nums[i] if 0 <= i < len(nums) else -1
            mx = nums[j] if 0 <= j < len(nums) else -1
            ans.append([mi, mx])
        return ans

        # def dfs(node, t):
        #     nonlocal mi, mx
        #     if node.val == t:
        #         mi = mx = t
        #         return [mi, mx]
        #     if node.val > t:        
        #         mx = node.val        
        #         if node.left:
        #             dfs(node.left, t)
        #     else:               
        #         mi = node.val
        #         if node.right:              
        #             dfs(node.right, t)
        #     return [mi, mx]

        # ans = []
        # hm = {}
        # for q in queries:
        #     mi, mx = -1, -1
        #     if q in hm:
        #         mi, mx = hm[q]
        #     else:
        #         dfs(root, q)
        #         hm[q] = [mi, mx]
        #     ans.append([mi, mx])
        # return ans
