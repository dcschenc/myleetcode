# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1530.Number%20of%20Good%20Leaf%20Nodes%20Pairs
        def dfs(node, level):
            if not node:
                return {}
            if not node.left and not node.right:
                return {node:level}            
            left = dfs(node.left, level + 1)
            right = dfs(node.right, level + 1)
            for l, r in list(product(left.keys(), right.keys())):
                if (l, r) in pairs:
                    continue
                dist = left[l] + right[r] - 2 * level
                if dist <= distance:
                    pairs.add((l, r))
            left.update(right)
            return left

        pairs = set()
        dfs(root, 0)
        return len(pairs)
