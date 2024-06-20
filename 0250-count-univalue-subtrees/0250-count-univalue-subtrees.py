# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None: return True
            isLeftUniValue = dfs(node.left)
            isRightUniValue = dfs(node.right)
            # If both the children form uni-value subtrees, we compare the value of
            # chidrens node with the node value.
            if isLeftUniValue and isRightUniValue:
                if node.left and node.val != node.left.val:
                    return False
                if node.right and node.val != node.right.val:
                    return False    
                self.count += 1
                return True
            # Else if any of the child does not form a uni-value subtree, the subtree
            # rooted at node cannot be a uni-value subtree.
            return False

        self.count = 0        
        dfs(root)
        return self.count


        # def get_trees(node):
        #     left, right = 0, 0
        #     is_same_left, is_same_right = True, True
        #     the_same_val = True
        #     if node.left:
        #         left, is_same_left = get_trees(node.left)
        #         if node.val != node.left.val:
        #             the_same_val = False
        #     if node.right:
        #         right, is_same_right = get_trees(node.right)
        #         if node.val != node.right.val:
        #             the_same_val = False
        #     if is_same_left and is_same_right and the_same_val:            
        #         return left + right + 1, True
        #     return left + right, False

        # node = root
        # if not node:
        #     return 0
        # cnt, _ = get_trees(node)
        # return cnt