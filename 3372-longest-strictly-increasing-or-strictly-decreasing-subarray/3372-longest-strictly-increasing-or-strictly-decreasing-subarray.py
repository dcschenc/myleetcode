class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n, ans = len(nums), 1
        for i in range(n-1):
            if nums[i + 1] > nums[i]:
                incr = True
            elif nums[i + 1] < nums[i]:
                incr = False
            else:
                continue

            for j in range(i + 1, n):
                if incr == True and nums[j] <= nums[j-1]:
                    break
                if incr == False and nums[j] >= nums[j-1]:
                    break
                ans = max(ans, j - i + 1)
        return ans
