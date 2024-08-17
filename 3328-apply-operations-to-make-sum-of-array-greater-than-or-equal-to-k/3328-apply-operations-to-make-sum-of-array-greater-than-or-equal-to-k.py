class Solution:
    def minOperations(self, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3091.Apply%20Operations%20to%20Make%20Sum%20of%20Array%20Greater%20Than%20or%20Equal%20to%20k
        ans = k
        for a in range(k):
            x = a + 1
            b = (k + x - 1) // x - 1
            ans = min(ans, a + b)
        return ans
        