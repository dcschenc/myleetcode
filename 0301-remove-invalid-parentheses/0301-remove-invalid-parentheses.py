class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def backtrack(index: int, left_remove: int, right_remove: int, left_count: int, right_count: int, path: str):
            if index == length:
                # Check if we no longer have any parentheses to remove and the parentheses are balanced
                if left_remove == 0 and right_remove == 0:
                    valid_expressions.add(path)
                return
          
            # Pruning: if there are more parentheses to remove than remaining characters
            # or more right parentheses used than left
            if length - index < left_remove + right_remove or left_count < right_count:
                return
          
            # Choose to ignore the current character if it's a parenthesis and we need to remove it
            if s[index] == '(' and left_remove > 0:
                backtrack(index + 1, left_remove - 1, right_remove, left_count, right_count, path)
            elif s[index] == ')' and right_remove > 0:
                backtrack(index + 1, left_remove, right_remove - 1, left_count, right_count, path)
          
            # Choose to keep the current character, updating the count of used parentheses
            backtrack(index + 1, left_remove, right_remove, left_count + (s[index] == '('), right_count + (s[index] == ')'), path + s[index])
      
        # Initial preparations
        left_remove, right_remove = 0, 0
        # First pass to find out the number of unmatched '(' and ')'
        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                # Only decrease the count of left parentheses if there's an unmatched left parenthesis
                if left_remove:
                    left_remove -= 1
                else:
                    right_remove += 1
      
        # A set to keep the unique valid expressions
        valid_expressions = set()
        length = len(s)
      
        # Start the DFS with the initial parameters
        backtrack(0, left_remove, right_remove, 0, 0, '')
      
        # Convert the set into a list and return it
        return list(valid_expressions)


        # def backtrack(idx, left, right, path):
        #     print(idx, left, right, path)
        #     nonlocal max_count
        #     if idx == n:
        #         if left == right:
        #             res.append(path)
        #             max_count = max(max_count, len(path))
        #         return
        #     if s[idx] == '(':
        #         backtrack(idx + 1, left + 1, right, path + s[idx])
        #     elif s[idx] == ')':
        #         if left > right:
        #             backtrack(idx + 1, left, right + 1, path + s[idx])
        #     # else:
        #     backtrack(idx + 1, left, right, path + s[idx])

        # n, res, max_count = len(s), [], -float('inf')
        # backtrack(0, 0, 0, '')
        # return [path for path in res if len(path) == max_count]
