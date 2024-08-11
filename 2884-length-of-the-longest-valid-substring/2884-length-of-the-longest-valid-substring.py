class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2781.Length%20of%20the%20Longest%20Valid%20Substring
        s = set(forbidden)
        ans = i = 0
        for j in range(len(word)):
            for k in range(j, max(j - 10, i - 1), -1):
                if word[k : j + 1] in s:
                    i = k + 1
                    break
            ans = max(ans, j - i + 1)
        return ans