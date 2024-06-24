class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/arithmetic-slices-ii-subsequence/editorial/
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        ans = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return ans


        # n = len(nums)
        # d = [defaultdict(int) for i in range(n)]
        # ans = 0
        # for i in range(n):
        #     for j in range(i):
        #         diff = nums[i] - nums[j]
        #         d[i][diff] = d[j][diff] + 1
        #         if d[i][diff] >= 2:
        #             if diff != 0:
        #                 ans += d[i][diff] - 1
        #             else:
        #                 for k in range(2, d[i][diff]):
        #                     ans += comb(d[i][diff], k)
        #                 # print(i, comb(d[i][diff], 2))
        # print(d)
        # return ans
