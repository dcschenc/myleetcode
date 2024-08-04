class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2393.Count%20Strictly%20Increasing%20Subarrays
        ans = i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] > nums[j - 1]:
                j += 1
            cnt = j - i
            ans += (1 + cnt) * cnt // 2
            i = j
        return ans

        n = len(nums)
        prectn = [1] * n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                prectn[i] += prectn[i-1]
        return sum(prectn)