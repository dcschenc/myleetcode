# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return None, 0
            left, d1 = dfs(node.left)
            right, d2 = dfs(node.right)
            if d1 > d2:
                return left, d1 + 1
            if d1 < d2:
                return right, d2 + 1
            return node, d1 + 1

        return dfs(root)[0]


        queue = deque()
        if root:
            queue.append(root)
            root.parent = root
        while queue:
            cur = []
            for i in range(len(queue)):                
                node = queue.popleft()
                cur.append(node)
                if node.left:
                    queue.append(node.left)
                    node.left.parent = node                    
                if node.right:
                    queue.append(node.right)
                    node.right.parent = node

        if len(queue) == 0:
            parent = cur[0].parent
            if len(cur) == 1:
                return cur[0]
            while True:
                found = True
                for i in range(len(cur)):
                    if cur[i].parent != parent:
                        found = False
                    cur[i] = cur[i].parent
                if found:
                    return parent
                parent = parent.parent                 