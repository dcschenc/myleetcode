class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        max_len = 0
        start = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:                        
                        max_len = max(max_len, i - stack[-1])
                    else:
                        max_len = max(max_len, i - start)
                else:
                    start = i
        return max_len
                    
        # max_length = 0
        # stack = [-1]  # Initialize a stack with -1

        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             max_length = max(max_length, i - stack[-1])

        # return max_length

        max_length = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    if i >= 2:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                else:
                    if i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                        if i - dp[i-1] >= 2:
                            dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                        else:
                            dp[i] = dp[i - 1] + 2

                max_length = max(max_length, dp[i])

        return max_length