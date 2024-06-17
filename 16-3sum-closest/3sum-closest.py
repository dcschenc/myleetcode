class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = pow(10,6)
        n = len(nums)
        nums.sort()
        three_element = []
        for i in range(n):
            left, right = i + 1, n-1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == target:
                    return three_sum
                if abs(three_sum-target) < res:
                    res = abs(three_sum-target)
                    three_element = [nums[i], nums[left], nums[right]]                
                if three_sum > target:
                    right -= 1
                else:
                    left += 1
        return sum(three_element)