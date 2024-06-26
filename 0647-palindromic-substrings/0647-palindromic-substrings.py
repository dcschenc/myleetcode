class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

                if dp[i][j]:
                    count += 1
        return count

        # def isPal(j, i):
        #     L, R = j, i
        #     while L < R:
        #         if s[L] == s[R]:
        #             L += 1
        #             R -= 1
        #         else:
        #             return False
        #     return True

        # n = len(s)
        # dp = [0] * n
        # dp[0] = 1
        # for i in range(1, n):
        #     dp[i] = dp[i-1] + 1
        #     for j in range(i):
        #         if isPal(j, i):
        #             dp[i] += 1
        # return dp[-1]
        def countPali(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res
        res = 0

        for i in range(len(s)):
            res += countPali(s, i, i)
            res += countPali(s, i, i + 1)
        return res

    

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # Check substrings of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1

        return count