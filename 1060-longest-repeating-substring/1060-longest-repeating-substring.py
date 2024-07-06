from collections import defaultdict
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1062.Longest%20Repeating%20Substring
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if i else 1
                    ans = max(ans, dp[i][j])
        return ans

        # S = s
        # def search(L: int, n: int, S: str) -> str:,
        #     """
        #     Search a substring of a given length
        #     that occurs at least 2 times.
        #     @return start position if the substring exists and -1 otherwise.
        #     """
        #     seen = set()
        #     for start in range(0, n - L + 1):
        #         tmp = S[start:start + L]
        #         if tmp in seen:
        #             return start
        #         seen.add(tmp)
        #     return -1

        # n = len(S)        
        # left, right = 1, n
        # while left <= right:
        #     L = left + (right - left) // 2
        #     if search(L, n, S) != -1:
        #         left = L + 1
        #     else:
        #         right = L - 1
               
        # return left - 1        

        # n = len(s)
        # hm = defaultdict(int)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         hm[s[i:j+1]] += 1
        # ans = [len(k) for k, v in hm.items() if v > 1]
        # return max(ans) if len(ans) > 0 else 0
