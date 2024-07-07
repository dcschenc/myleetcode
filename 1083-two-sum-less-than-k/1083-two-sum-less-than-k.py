class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = -1
        while left < right:
            cur = nums[left] + nums[right]
            if cur < k:
                max_sum = max(max_sum, cur)
                left += 1
            else:
                right -= 1
        return max_sum

        # max_sum = -1
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < k:
        #             max_sum = max(max_sum, nums[i] + nums[j])
        # return max_sum
