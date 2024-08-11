class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2760.Longest%20Even%20Odd%20Subarray%20With%20Threshold
        ans, n = 0, len(nums)
        for l in range(n):
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                r = l + 1
                while r < n and nums[r] % 2 != nums[r - 1] % 2 and nums[r] <= threshold:
                    r += 1
                ans = max(ans, r - l)
        return ans

        # n = len(nums)
        # mx = 0
        # for i in range(n):
        #     if nums[i] % 2 != 0 or nums[i] > threshold:
        #         continue
        #     mx = max(mx, 1)
        #     for j in range(i + 1, n):
        #         if nums[j] % 2 == nums[j-1] % 2:
        #             break
        #         if nums[j] > threshold:
        #             break
        #         mx = max(mx, j - i + 1) 
        # return mx
