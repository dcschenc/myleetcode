# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(node, path, cur_sum):
            if not node:
                return

            # Update the current sum
            cur_sum += node.val

            # Append the current node to the path
            path.append(node.val)

            # Check if it's a leaf node and if the path sum matches the target
            if not node.left and not node.right and cur_sum == targetSum:
                result.append(path.copy())

            # Recursively explore the left and right subtrees
            dfs(node.left, path, cur_sum)
            dfs(node.right, path, cur_sum)

            # Backtrack: remove the last node from the path
            path.pop()

        result = []
        dfs(root, [], 0)
        return result

        # def dfs(node, curr):
        #     if not node:
        #         return
        #     curr.append(node.val)
        #     if node.left:
        #         dfs(node.left, curr[:])
        #     if node.right:
        #         dfs(node.right, curr[:])
        #     if not node.left and not node.right:
        #         if sum(curr) == targetSum:
        #             res.append(curr)

        # res = []
        # dfs(root, [])
        # return res