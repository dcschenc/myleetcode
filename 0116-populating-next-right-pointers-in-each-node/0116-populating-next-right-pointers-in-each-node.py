"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            level_size = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                if i < level_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


        ########### similar to using queue ############
        # if root == None:
        #     return None
        # levels = [root]
        # while len(levels) > 0:
        #     curr_level = []
        #     for node in levels:                
        #         if node.left:
        #             curr_level.append(node.left)
        #         if node.right:
        #             curr_level.append(node.right)
        #     if len(curr_level) > 0:
        #         pre_node = curr_level[0]
        #         for c_node in curr_level[1:]:
        #             pre_node.next = c_node
        #             pre_node = c_node
        #         pre_node = None
        #     levels = curr_level
        # return root
                