class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # Initialize the outDegree (children) - inDegree (parent) to 1
        degree = 1
        
        # Iterate through the nodes in the preorder traversal
        for node in preorder.split(','):
            degree -= 1 # Decrement the degree by 1 for each node
            
            if degree < 0: # If the degree is negative, return False
                return False
            
            if node != '#': # If the node is not a leaf node
                degree += 2 # Increment the degree by 2 for each non-leaf node
            
        # If the final degree is 0, the tree is valid, else invalid
        return degree == 0
        
        # nodes = preorder.split(',')
        # slots = 1  # Start with one slot for the root node

        # for node in nodes:
        #     slots -= 1  # Consume one slot for the current node

        #     if slots < 0:
        #         return False  # Not enough slots for the current subtree

        #     if node != '#':
        #         slots += 2  # Each non-null node adds two slots for its children

        # return slots == 0  # All slots should be used up at the end

        # if len(preorder) == 0:
        #     return True

        preorder = preorder.split(',')
        stack = [preorder[0]]
        idx = 1
        while stack and idx < len(preorder):
            stack.append(preorder[idx])
            idx += 1
            while len(stack) >= 3 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack[-1] = '#'
        if len(stack) == 1 and stack[0] == '#':
            return True
        return False
                    
