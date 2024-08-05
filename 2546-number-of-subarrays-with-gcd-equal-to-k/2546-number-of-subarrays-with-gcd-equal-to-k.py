class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2447.Number%20of%20Subarrays%20With%20GCD%20Equal%20to%20K
        n, ans = len(nums), 0
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == k:
                    ans += 1
        return ans