"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def dfs(node):
            if len(node.children) == 0:
                return 0
            cur = []
            for c in node.children:
                cur.append(1 + dfs(c))

            cur.sort(reverse=True)
            if len(cur) > 1:
                ans[0] = max(ans[0], cur[0] + cur[1])
            else:
                ans[0] = max(ans[0], cur[0])
            return cur[0]

        ans = [0]
        dfs(root)
        return ans[0]