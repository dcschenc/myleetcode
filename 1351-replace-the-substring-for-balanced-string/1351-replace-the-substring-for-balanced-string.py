class Solution:
    def balancedString(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1234.Replace%20the%20Substring%20for%20Balanced%20String
        # Setup of the Counter with character frequencies
        cnt = Counter(s)
        n = len(s)
        # Early check for balance
        if all(v <= n // 4 for v in cnt.values()):
            return 0
        ans, j = n, 0
        # Traverse the string with i pointer
        for i, c in enumerate(s):
            cnt[c] -= 1  # Decrement count for current character
            # Inner loop to shrink the sliding window and update the minimum answer
            while j <= i and all(v <= n // 4 for v in cnt.values()):
                ans = min(ans, i - j + 1)
                cnt[s[j]] += 1  # Increment count as we leave the current character out of the window
                j += 1
        # Return the smallest window length found
        return ans