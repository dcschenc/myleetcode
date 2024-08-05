# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2471.Minimum%20Number%20of%20Operations%20to%20Sort%20a%20Binary%20Tree%20by%20Level
        queue = deque([root])
        levels = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(cur)
        
        ans = 0
        for cur in levels:
            sort = sorted(cur)
            n = len(cur)
            hm = {}
            for i in range(n):
                hm[cur[i]] = i            
            for i in range(n):                
                if cur[i] != sort[i]:
                    ans += 1
                    j = hm[sort[i]]
                    cur[j], cur[i] = cur[i], cur[j]
                    hm[cur[j]] = j
                    hm[cur[i]] = i                
        return ans