class Solution:
    # https://leetcode.com/problems/unique-substrings-in-wraparound-string/solutions/493713/python-solution-with-explanation/
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26
        k = 0
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                k += 1
            else:
                k = 1
            idx = ord(s[i]) - ord('a')
            dp[idx] = max(dp[idx], k)
        # print(dp)
        return sum(dp)