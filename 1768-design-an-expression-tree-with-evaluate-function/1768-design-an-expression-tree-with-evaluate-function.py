import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):    
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class MyNode(Node):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        operator = self.val
        left = self.left.evaluate()
        right = self.right.evaluate()
        if operator == '+':
            return left + right 
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        else:
            return left//right

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        stk = []
        for s in postfix:
            node = MyNode(s)
            if not s.isdigit():
                node.right = stk.pop()
                node.left = stk.pop()
            stk.append(node)
        return stk[-1]        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        