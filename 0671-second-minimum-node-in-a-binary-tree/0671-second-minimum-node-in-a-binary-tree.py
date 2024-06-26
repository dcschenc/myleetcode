# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0671.Second%20Minimum%20Node%20In%20a%20Binary%20Tree
        def dfs(node):
            if not node: return
            nonlocal ans, v
            if node.val > v:
                ans = node.val if ans == -1 else min(ans, node.val)
            dfs(node.left)
            dfs(node.right)

        ans, v = -1, root.val
        dfs(root)
        return ans
        # if root is None or root.left is None:
        #     return -1
        # queue = deque()
        # queue.append(root)        
        # res = None
        # # If we cant assume its BST, we need to traversal on all nodes.
        # # We will write a BFS and the "operation" will be to save the minimal element   which is bigger than "root.val".
        # #  root val is always the smallest
        # while queue:
        #     cur = queue.popleft()
        #     if res is None and cur.val > root.val:
        #         res = cur.val
        #     elif res and cur.val < res and cur.val > root.val:
        #         res = cur.val

        #     if cur.left:
        #         queue.append(cur.left)
        #     if cur.right:
        #         queue.append(cur.right)        
        
        # return -1 if res is None else res