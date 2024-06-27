# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0742.Closest%20Leaf%20in%20a%20Binary%20Tree

        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if not node: return
            g[node].append(parent)
            g[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)

        g = defaultdict(list)
        dfs(root, None)
        queue = deque(node for node in g if node and node.val == k)
        vis = set(queue)
        while queue:
            node = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return node.val
                for nxt in g[node]:
                    if nxt not in vis:
                        vis.add(nxt)
                        queue.append(nxt)

        # def dfs(node, level, ischild):     
        #     nonlocal target_level       
        #     if not node.left and not node.right:
        #          hm[node.val] = (level, ischild)
        #     if node.val == k:  
        #         ischild = True   
        #         target_level = level
        #     if node.left:
        #         dfs(node.left, level + 1, ischild)
        #     if node.right:
        #         dfs(node.right, level + 1, ischild)
        
        # hm = {}
        # target_level = -1
        # dfs(root, 1, False)
        # ans = [float('inf'), -1]
        # # print(hm, target_level)
        # for val, (level, ischild) in hm.items():
        #     if val == k:
        #         return val
        #     if ischild:
        #         if ans[0] > level - target_level:
        #             ans = [level - target_level, val]
        #     else:
        #         if ans[0] > target_level + level - 2:
        #             ans = [target_level + level - 2, val]
        # return ans[1]
        
