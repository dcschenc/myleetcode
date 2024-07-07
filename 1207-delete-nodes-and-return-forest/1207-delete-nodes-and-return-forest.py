# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1110.Delete%20Nodes%20And%20Return%20Forest
        def dfs(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            root.left, root.right = dfs(root.left), dfs(root.right)
            if root.val not in s:
                return root
            if root.left:
                ans.append(root.left)
            if root.right:
                ans.append(root.right)
            return None

        s = set(to_delete)
        ans = []
        if dfs(root):
            ans.append(root)
        return ans
        

        def dfs(node, parent, left):
            if node in roots and node.val not in to_delete:
                ans.append(node)
            if node.val in to_delete:                
                if node.left:
                    roots.append(node.left)
                if node.right:
                    roots.append(node.right)
                if parent and left:
                    parent.left = None
                if parent and not left:
                    parent.right = None
            if node.left:
                dfs(node.left, node, True)
            if node.right:
                dfs(node.right, node, False)

        ans = []
        roots = [root]
        to_delete = set(to_delete)
        dfs(root, None, False)            
        return ans