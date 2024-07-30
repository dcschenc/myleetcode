class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2090.K%20Radius%20Subarray%20Averages
        n = len(nums)
        avgs = [-1] * n
        if n < 2 * k + 1: return avgs
        total_sum = sum(nums[:2 * k + 1])
        avgs[k] = total_sum // (2 * k + 1)

        for i in range(k + 1, n - k):
            total_sum += nums[i + k] - nums[i - k - 1]
            avgs[i] = total_sum // (2 * k + 1)

        return avgs

        # cur_sum = 0
        # n = len(nums)
        # ans = []
        # presum = [0] * len(nums)
        # presum[0] = nums[0]
        # for i in range(1,len(nums)):
        #     presum[i] += presum[i-1] + nums[i]

        # for i in range(len(nums)):
        #     if i-k < 0 or i + k > n-1:
        #         ans.append(-1)
        #         continue

        #     if i-k-1 < 0:
        #         cur_sum = presum[i+k]
        #     else:
        #         cur_sum = presum[i+k] - presum[i-k-1]
        #     ans.append(int(cur_sum/(2*k+1)))
        # return ans