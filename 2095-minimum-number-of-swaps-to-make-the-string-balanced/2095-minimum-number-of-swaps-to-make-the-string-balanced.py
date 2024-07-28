class Solution:
    def minSwaps(self, s: str) -> int:
        # https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/solutions/4666171/python3-stack-with-explanation/
        stack = []
        mismatch = 0
        for char in s:
            if char == '[':
                stack.append(char)
            # Every time we find a valid paren, we remove it from the stack as we dont
            # need any swaps there
            elif char == ']':
                if len(stack) > 0 :
                    stack.pop()
                # If there is an invalid paren, we increment a mismatch counter.
                else:
                    mismatch += 1
        return (mismatch + 1) // 2