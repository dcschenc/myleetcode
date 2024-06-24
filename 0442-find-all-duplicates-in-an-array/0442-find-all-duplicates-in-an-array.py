class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # in-place marking algorithm. It operates directly on the input array without using additional data structures to identify and collect duplicate elements
        result = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                result.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        # Restore the original array by undoing the marks.
        # for num in nums:
        #     if num < 0:
        #         idx = abs(num) - 1
        #         nums[idx] = -nums[idx]
        return result