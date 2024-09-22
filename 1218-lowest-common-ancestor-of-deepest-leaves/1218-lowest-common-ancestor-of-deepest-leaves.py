# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1123.Lowest%20Common%20Ancestor%20of%20Deepest%20Leaves
        def dfs(node):
            if node is None:
                return None, 0
            l, d1 = dfs(node.left)
            r, d2 = dfs(node.right)
            if d1 > d2:
                return l, d1 + 1
            if d1 < d2:
                return r, d2 + 1
            return node, d1 + 1  ## d1 == d2

        return dfs(root)[0]

        # # Tag each node with it's depth.        
        # def dfs(node, parent = None):
        #     if node:
        #         depth[node] = depth[parent] + 1
        #         dfs(node.left, node)
        #         dfs(node.right, node)

        # def answer(node):
        #     # Return the answer for the subtree at node.
        #     if not node or depth.get(node, None) == max_depth:
        #         return node
        #     left, right = answer(node.left), answer(node.right)
        #     if left and right:
        #         return node
        #     if left:
        #         return left
        #     if right:
        #         return right

        # depth = {None: -1}
        # dfs(root)

        # max_depth = max(depth.values())
        # return answer(root)