class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2256.Minimum%20Average%20Difference
        total = sum(nums)
        n = len(nums)
        prefixSum = 0
        min_diff = 10 ** 5+1
        idx = -1
        for i, num in enumerate(nums):
            prefixSum += num
            if i == n-1:
                diff = prefixSum // (i+1)
            else:
                diff = abs(prefixSum // (i+1) - (total - prefixSum) // (n-i-1))
            # print(i, diff)
            if  diff < min_diff:
                min_diff = diff
                idx = i
        return idx
        

