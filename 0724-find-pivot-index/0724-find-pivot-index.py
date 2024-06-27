class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        
        for i, num in enumerate(nums):
            right_sum -= num            
            if left_sum == right_sum:
                return i            
            left_sum += num        
        return -1
        
        # sum_left, sum_right = nums[:], nums[:]
        # for i in range(1, len(nums)):
        #     sum_left[i] += sum_left[i-1]
        # for i in range(len(nums)-2, -1, -1):
        #     sum_right[i] += sum_right[i+1]
        # for i in range(len(nums)):
        #     if sum_left[i] == sum_right[i]:
        #         return i
        # # print(sum_left, sum_right)
        # return -1
            
