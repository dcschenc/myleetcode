class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2654.Minimum%20Number%20of%20Operations%20to%20Make%20All%20Array%20Elements%20Equal%20to%201
        n = len(nums)
        cnt = nums.count(1)
        if cnt:
            return n - cnt
        mi = n + 1
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    mi = min(mi, j - i + 1)
        return -1 if mi > n else n - 1 + mi - 1
