class Solution:
    def countHomogenous(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1759.Count%20Number%20of%20Homogenous%20Substrings
        mod = 10**9 + 7
        i, n = 1, len(s)
        ans = 1
        cnt = 1
        while i < n:
            if s[i] != s[i-1]:
                cnt = 1
            else:
                cnt += 1
            ans += cnt
            i += 1
        return ans % mod


        prev = 0
        ans = 0
        while i <= n:
            if i == n or s[i] != s[prev]:
                cnt = i - prev
                ans += cnt * (cnt + 1) // 2
                prev = i
            i += 1
        return ans % mod