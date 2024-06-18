# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # if not root:
        #     return []
        # levels = [root]
        # while len(levels) > 0:
        #     # res.append(levels)
        #     res.append([])
        #     next_level = []
        #     for node in levels:
        #         res[-1].append(node.val)                
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
            
        #     levels = next_level
        # return res

        ######## BSF & QUEUE ########
        res = []
        if not root: 
            return None
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            res.append(level)        
        return res