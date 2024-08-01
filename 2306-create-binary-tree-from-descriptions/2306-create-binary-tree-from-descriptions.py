# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2196.Create%20Binary%20Tree%20From%20Descriptions
        hm, children = {}, set()
        for p, c, l in descriptions:
            children.add(c)
            child = TreeNode(c)
            if c in hm:
                child = hm[c]
            else:
                hm[c] = child
                                
            parent = TreeNode(p)
            if p in hm:
                parent = hm[p]
            else:                
                hm[p] = parent
            if l == 1:
                parent.left = child
            else:
                parent.right = child
        
        for k in hm.keys():
            if k not in children:
                return hm[k]

        