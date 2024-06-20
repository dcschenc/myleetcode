class Solution:
    def countDigitOne(self, n: int) -> int:
        # https://leetcode.com/problems/number-of-digit-one/solutions/3230126/233-solution-with-step-by-step-explanation/
        ans = 0

        pow10 = 1
        while pow10 <= n:
            divisor = pow10 * 10
            quotient = n // divisor
            remainder = n % divisor
            if quotient > 0:
                ans += quotient * pow10
            if remainder >= pow10:
                ans += min(remainder - pow10 + 1, pow10)
            pow10 *= 10

        return ans