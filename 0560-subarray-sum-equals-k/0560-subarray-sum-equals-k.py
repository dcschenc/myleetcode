class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0560.Subarray%20Sum%20Equals%20K
        presum = Counter({0: 1})
        ans = s = 0
        for x in nums:
            s += x
            ans += presum[s - k]
            presum[s] += 1
        return ans


        # prefix_sum = [0] * len(nums)
        curSum= 0
        prefixSum = {0:1}
        count = 0
        for i in range(len(nums)):
            curSum += nums[i]
            # if curSum - k in prefixSum:
            #     count += hm[curSum-k]
            count += prefixSum.get(curSum - k, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return count
