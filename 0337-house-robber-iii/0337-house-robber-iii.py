# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return (0, 0)  # (current_node_value_not_robbed, current_node_value_robbed)

            left = dfs(node.left)
            right = dfs(node.right)

        # If current node is not robbed, maximum value is the sum of maximum values from its children
            not_robbed = max(left) + max(right)

            # If  current node is robbed, maximum value is the sum of values from its children and the current node's value
            robbed = node.val + left[0] + right[0]

            return (not_robbed, robbed)

        result = dfs(root)
        
        # The maximum value is the maximum of the two cases (robbed or not robbed) for the root
        return max(result)

        # if not root:
        #     return 0
        # # reform tree into array-based tree
        # tree = []
        # graph = {-1: []}
        # index = -1
        # q = [(root, -1)]
        # while q:
        #     node, parent_index = q.pop(0)
        #     if node:
        #         index += 1
        #         tree.append(node.val)
        #         graph[index] = []
        #         graph[parent_index].append(index)
        #         q.append((node.left, index))
        #         q.append((node.right, index))
        # # represent the maximum start by node i with robbing i
        # dp_rob = [0] * (index+1)
        # # represent the maximum start by node i without robbing i
        # dp_not_rob = [0] * (index+1)
        # for i in reversed(range(index+1)):
        #     if not graph[i]: # if is leaf
        #         dp_rob[i] = tree[i]
        #         dp_not_rob[i] = 0
        #     else:
        #         dp_rob[i] = tree[i] + sum(dp_not_rob[child] for child in graph[i])
        #         dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child]) for child in graph[i])
        # return max(dp_rob[0], dp_not_rob[0])

        # memo = {}
        
        # def robbing(root):
        #     if not root: return 0
        #     # Since we call robing for node.left and also node.left.left, when the recursion 
        #     # runs for node.left it will call its child which will be node.left.left. 
        #     # So we will be running same exploration twice leading to lot of extra calls 
        #     # So we store in memo.
        #     if root in memo: return memo[root]

        #     # When we rob root, we can't rob root.left and root.right. So we have to 
        #     # convsider grand children. We will have 4 grandchildren. 
        #     withRoot = root.val 
        #     if root.left: 
        #         leftLeft, leftRight = root.left.left, root.left.right 
        #         withRoot += robbing(leftLeft) + robbing(leftRight)    
        #     if root.right:
        #         rightLeft, rightRight = root.right.left, root.right.right
        #         withRoot += robbing(rightLeft) + robbing(rightRight)
            
        #     # If we do not rob root then we can rob left and right child 
        #     withChildren = robbing(root.left) + robbing(root.right)

        #     memo[root] = max(withRoot, withChildren)
        #     return memo[root]
        
        # return robbing(root)

        # queue = deque()
        # if root:
        #     queue.append((root, [0, root.val]))
        # dp = []

        # while queue:
        #     dp = []
        #     for i in range(len(queue)):
        #         node, p_dp = queue.popleft()
        #         # print(p_dp)               
        #         node_dp = max(node.val + p_dp[-2], p_dp[-1])
        #         p_dp.append(node_dp)
        #         if node.left:
        #             queue.append((node.left, p_dp))
        #         if node.right:
        #             queue.append((node.right, p_dp))
        #         dp.append(node_dp)
        #     print(dp)
        # # print(dp)
        # return sum(dp)

