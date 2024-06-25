# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        def dfs(s):
            if not s: return None
            p = s.find('(')
            if p == -1:
                return TreeNode(int(s))
            root = TreeNode(int(s[:p]))
            start = p
            cnt = 0
            for i in range(p, len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                    
                if cnt == 0:
                    if start == p:
                        root.left = dfs(s[start + 1 : i])
                        start = i + 1
                    else:
                        root.right = dfs(s[start + 1 : i])
            return root

        return dfs(s)
        
        def construct_tree(start, end):
            i = start
            val = ''
            while i <= end and (s[i].isdigit() or s[i] == '-'):
                i += 1
            root = TreeNode(int(s[start:i]))

            j = -1
            if i <= end and s[i] == '(':
                j = i + 1
                count = 1
                while count > 0:
                    if s[j] == '(':
                        count += 1
                    elif s[j] == ')':
                        count -= 1
                    j += 1
                root.left = construct_tree(i + 1, j - 2)

            if j <= end and s[j] == '(':
                root.right = construct_tree(j + 1, end - 1)

            return root            

        if s == '':
            return None
        return construct_tree(0, len(s) - 1)

