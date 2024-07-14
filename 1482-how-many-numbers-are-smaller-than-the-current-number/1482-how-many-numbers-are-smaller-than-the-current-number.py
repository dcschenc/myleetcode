class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def find_idx(num):
            left, right = 0, len(sorted_nums) - 1
            while left < right:
                mid = (left + right) // 2
                if sorted_nums[mid] >= num:
                    right = mid
                else:
                    left = mid + 1           
            return left

        sorted_nums = sorted(nums)
        ans = []
        for i, num in enumerate(nums):
            ans.append(find_idx(num))   
        return ans
