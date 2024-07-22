"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1650.Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree%20III
        seen = set()
        node = p
        while node:
            seen.add(node)
            node = node.parent
        node = q
        while node not in seen:
            node = node.parent
        return node
        
        pp = [p]
        pq = [q]
        while p.parent:
            pp.append(p.parent)
            p = p.parent
        while q.parent:
            pq.append(q.parent)
            q = q.parent
        pq = set(pq)
        for node in pp:
            if node in pq:
                return node
