class Solution:
    def smallestFactorization(self, num: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0625.Minimum%20Factorization
        if num < 2:
            return num
        ans, mul = 0, 1
        for i in range(9, 1, -1):
            while num % i == 0:
                num = num // i
                ans += i * mul
                mul *= 10
        return ans if num < 2 and ans <= 2 ** 31 - 1 else 0 


        