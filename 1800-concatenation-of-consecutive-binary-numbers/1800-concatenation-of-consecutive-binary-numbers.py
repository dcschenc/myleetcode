class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1680.Concatenation%20of%20Consecutive%20Binary%20Numbers
        ans = 0
        i = 1
        while i < n + 1:
            cnt = len(bin(i)) - 2
            ans = ans << cnt
            ans += i
            ans = ans % (10**9 + 7)
            i += 1
        return ans % (10**9 + 7)