class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        x, y = nlargest(2, nums)
        return nums.index(x) if x >= 2 * y else -1
        
        # f_max = s_max = -1
        # max_i = 0
        # for i, val in enumerate(nums):
        #     if val >= f_max:
        #         f_max, s_max = val, f_max
        #         max_i = i
        #     elif val > s_max:
        #         s_max = val
        # if f_max < 2*s_max:
        #     return -1
        # return max_i
        
        
        
        # max_i = 0
        # for i in range(len(nums)):
        #     if nums[i] > nums[max_i]:
        #         max_i = i
        # for i in range(len(nums)):
        #     if i != max_i:
        #         if nums[i] * 2 > nums[max_i]:
        #             return -1
        # return max_i
                