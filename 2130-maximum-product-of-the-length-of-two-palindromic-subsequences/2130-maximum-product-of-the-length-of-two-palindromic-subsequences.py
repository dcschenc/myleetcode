class Solution:
    def maxProduct(self, s: str) -> int:      
        def is_palindromic(candidate):
            left, right = 0, len(candidate) - 1
            while left < right:
                if candidate[left] != candidate[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(idx, s1, s2):
            # print(idx, s1, s2)
            if is_palindromic(s1) and is_palindromic(s2):
                ans[0] = max(ans[0], len(s1) * len(s2))
            if idx == n:
                return
            backtrack(idx + 1, s1 + s[idx], s2)
            backtrack(idx + 1, s1, s2 + s[idx])
            backtrack(idx + 1, s1, s2)

        ans, n = [0], len(s)
        backtrack(0, '', '')
        return ans[0]

        # n = len(s)
        # p = [True] * (1 << n)
        # for k in range(1, 1 << n):
        #     i, j = 0, n - 1
        #     while i < j:
        #         while i < j and (k >> i & 1) == 0:
        #             i += 1
        #         while i < j and (k >> j & 1) == 0:
        #             j -= 1
        #         if i < j and s[i] != s[j]:
        #             p[k] = False
        #             break
        #         i, j = i + 1, j - 1
        # ans = 0
        # for i in range(1, 1 << n):
        #     if p[i]:
        #         mx = ((1 << n) - 1) ^ i
        #         j = mx
        #         a = i.bit_count()
        #         while j:
        #             if p[j]:
        #                 b = j.bit_count()
        #                 ans = max(ans, a * b)
        #             j = (j - 1) & mx
        # return ans