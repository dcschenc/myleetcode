# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def dfs(self, node):
        if node.left:
            node.left.val = 2 * node.val + 1
            self.hm.add(node.left.val)
            self.dfs(node.left)
        if node.right:
            node.right.val = 2 * node.val + 2
            self.hm.add(node.right.val)
            self.dfs(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.hm = set([0])
        self.dfs(root)        
        

    def find(self, target: int) -> bool:
        return target in self.hm
        # def dfs(node):
        #     if not node:
        #         return False
        #     if node.val == target:
        #         return True
        #     if dfs(node.left):
        #         return True
        #     if dfs(node.right):
        #         return True
        #     return False

        # if target in self.hm: 
        #     return self.hm[target]

        # ans = dfs(self.root)
        # if ans:
        #     self.hm[target] = True
        #     return True
        # self.hm[target] = False
        # return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)