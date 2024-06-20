# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    hm = {}
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1644.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20II
        # def dfs(node):
        #     if node is None:
        #         return False
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     if left and right:
        #         ans[0] = node
        #     if (left or right) and (node.val == p.val or node.val == q.val):
        #         ans[0] = node
        #     return left or right or node.val == p.val or node.val == q.val

        # ans = [None]
        # dfs(root)
        # return ans[0]

        def dfs(node):
            if node is None or node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
                
        return dfs(root)

        
    #     node = root
    #     if node.val == p.val or node.val == q.val:
    #         return node
    #     if self.find_node(node.left, p.val):
    #         if self.find_node(node.right, q.val):
    #             return node
    #         else:
    #             return self.lowestCommonAncestor(node.left, p, q)
    #     else:
    #         if self.find_node(node.left, q.val):
    #             return node
    #         else:
    #             return self.lowestCommonAncestor(node.right, p, q)
            
    # def find_node(self, node, target):           
    #     if (node,target) in self.hm:
    #         return self.hm[(node,target)]
    #     if not node:
    #         res = False
    #     elif node.val == target:
    #         res = True
    #     elif self.find_node(node.left, target) or self.find_node(node.right, target):
    #         res = True
    #     else:
    #         res = False
    #     self.hm[(node,target)] = res
    #     return res
       
        
    