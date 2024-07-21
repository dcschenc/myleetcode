class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1638.Count%20Substrings%20That%20Differ%20by%20One%20Character
        ans = 0
        m, n = len(s), len(t)
        for i, a in enumerate(s):
            for j, b in enumerate(t):
                if a != b:
                    l = r = 0
                    while i > l and j > l and s[i - l - 1] == t[j - l - 1]:
                        l += 1
                    while i + r + 1 < m and j + r + 1 < n and s[i + r + 1] == t[j + r + 1]:
                        r += 1
                    ans += (l + 1) * (r + 1)
        return ans