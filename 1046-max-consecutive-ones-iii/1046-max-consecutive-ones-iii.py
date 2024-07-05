class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, max_length, max_ones = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1                
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_length = max(max_length, right - left + 1)
            # max_ones = max(max_ones, max_length)
        return max_length
