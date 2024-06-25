# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:   
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            hm[total] += 1
            return total
            # if not node.left and not node.right:
            #     hm[node.val] += 1
            #     return node.val
            # s = node.val
            # if node.left:
            #     s += get_sum(node.left)
            # if node.right:
            #     s += get_sum(node.right)
            # hm[s] += 1
            # return s        
        if not root: return []
        hm = defaultdict(int)
        dfs(root)
        max_count = max(hm.values())
        res = [key for key, value in hm.items() if value == max_count]
        # hm = sorted(hm.items(), key=lambda x: x[1], reverse=True)
        # res = []
        # for k, v in hm:
        #     if not res or count == v:
        #         res.append(k)
        #         count = v
        return res

        