# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        if not p and not q:
            return True
        if not p and q or not q and p:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        stack_1, stack_2 = [p], [q]
        while stack_1 and stack_2:
            p = stack_1.pop()
            q = stack_2.pop()
            if not p and not q:
                continue
            if not p and q or not q and p:
                return False
            if p.val != q.val:
                return False
            # if p.left:
            stack_1.append(p.left)
            # if p.right:
            stack_1.append(p.right)
            # if q.left:
            stack_2.append(q.left)
            # if q.right:
            stack_2.append(q.right)
                
        if stack_1 or stack_2:
            return False
        return True