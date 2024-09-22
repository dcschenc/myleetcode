class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1111.Maximum%20Nesting%20Depth%20of%20Two%20Valid%20Parentheses%20Strings
        res = []
        depth = 0
        
        for char in seq:
            if char == '(':
                depth += 1
                res.append(depth % 2)  # Assign 0 or 1 based on the current depth
            else:
                res.append(depth % 2)  # Assign 0 or 1 based on the current depth
                depth -= 1
                
        return res
        
        ans = [0] * len(seq)
        x = 0
        for i, c in enumerate(seq):
            if c == "(":
                ans[i] = x & 1
                x += 1
            else:
                x -= 1
                ans[i] = x & 1
        return ans
        
        # Initialize an array to store the assignment of depths to each parenthesis.
        ans = [0] * len(seq)
      
        # Declare a variable to keep track of the current depth level.
        depth_level = 0
      
        # Iterate over each character in the sequence alongside its index.
        for index, char in enumerate(seq):
            if char == "(":
                # If the parenthesis is an opening one, determine the depth.
                # We use bitwise AND with 1 to alternate between 0 and 1.
                ans[index] = depth_level & 1
                # Increment depth level since we've encountered an opening parenthesis.
                depth_level += 1
            else:
                # If the parenthesis is a closing one, first decrement the depth level.
                depth_level -= 1
                # After decreasing the depth level, determine the depth for the closing parenthesis.
                ans[index] = depth_level & 1
      
        # Return the final array with the assigned depths.
        return ans