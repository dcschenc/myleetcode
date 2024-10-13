class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2210.Count%20Hills%20and%20Valleys%20in%20an%20Array
        ans = j = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] > nums[j] and nums[i] > nums[i + 1]:
                ans += 1
            if nums[i] < nums[j] and nums[i] < nums[i + 1]:
                ans += 1
            j = i
        return ans