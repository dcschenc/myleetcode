class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2370.Longest%20Ideal%20Subsequence
        n = len(s)
        ans = 1
        dp = [1] * n
        d = {s[0]: 0}
        for i in range(1, n):
            a = ord(s[i])
            for b in ascii_lowercase:
                if abs(a - ord(b)) > k:
                    continue
                if b in d:
                    dp[i] = max(dp[i], dp[d[b]] + 1)
            d[s[i]] = i
        return max(dp)

        n = len(s)
        dp = defaultdict(int)
        for i in range(n):            
            c = s[i]
            if c in dp:
                dp[c] = dp[c] + 1
            for j in range(-k, k + 1):
                if j == 0: continue
                prev = chr(ord(c) + j)
                if prev in dp:
                    dp[c] = max(dp[c], dp[prev] + 1)
            if dp[c] == 0:
                dp[c] = 1
            
        return max(dp.values())

        # Time Limit Exceeded
        n = len(s)
        dp = [1] * n
        for i in range(1, n):            
            for j in range(i):
                if abs(ord(s[i]) - ord(s[j])) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # n = len(s)
        # ans = 1
        # dp = [1] * n
        # d = {s[0]: 0}
        # for i in range(1, n):
        #     a = ord(s[i])
        #     for b in ascii_lowercase:
        #         if abs(a - ord(b)) > k:
        #             continue
        #         if b in d:
        #             dp[i] = max(dp[i], dp[d[b]] + 1)
        #     d[s[i]] = i
        # return max(dp)