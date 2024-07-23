class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1712.Ways%20to%20Split%20Array%20Into%20Three%20Subarrays
        mod = 10**9 + 7
        s = list(accumulate(nums))
        # print(s)
        ans, n = 0, len(nums)
        for i in range(n - 2):
            j = bisect_left(s, s[i] << 1, i + 1, n - 1)
            k = bisect_right(s, (s[-1] + s[i]) >> 1, j, n - 1)
            ans += k - j
        return ans % mod

        # mod = 10 ** 9 + 7
        # n = len(nums)
        # presum = [0] * (n)
        # for i in range(n):
        #     presum[i] = nums[i]
        #     if i > 0:
        #         presum[i] += presum[i-1]
        # ans = 0
        # for i in range(n-2):          
        #    j = bisect_left(presum, presum[i] << 1, i + 1, n-1)  ## the leftmost idx the middle part can be
        #    k = bisect_right(presum, (presum[-1] + presum[i]) >> 1, j, n-1)  ## the right most idx the last part must begin
        #    ans += (k - j)
        # return ans % mod
           


