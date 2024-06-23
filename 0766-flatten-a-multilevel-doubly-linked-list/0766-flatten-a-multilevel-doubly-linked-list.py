"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':   
        def dfs(node):
            prev = None
            while node:
                if node.child is None:
                    prev = node
                    node = node.next
                else:
                    right = node.next
                    node.next = node.child
                    node.child.prev = node
                    last_child = dfs(node.child)
                    last_child.next = right
                    if right:
                        right.prev = last_child
                    node.child = None
                    node = right
                    prev = last_child
            return prev
    
        if head is None:
            return head
        # node = head
        dfs(head)
        return head
        
    

        # if not head:
        #     return None

        # dummy = Node(0)
        # dummy.next = head
        # stack = [head]
        # prev = dummy

        # while stack:
        #     cur = stack.pop()

        #     if cur.next:
        #         stack.append(cur.next)

        #     if cur.child:
        #         stack.append(cur.child)
        #         cur.child = None

        #     prev.next = cur
        #     cur.prev = prev
        #     prev = cur

        # dummy.next.prev = None
        # return dummy.next
        
        
        # child = node.child
        # right = node.next
        # node.next = child
        # child.prev = node
        # if child.child:
        #     child_last = get_childs(child)
        #     child_last.next = right
        # else:
        #     child = child.next
        
        