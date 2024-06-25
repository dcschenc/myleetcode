# from collections import default
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0496.Next%20Greater%20Element%20I
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = [next_greater.get(num, -1) for num in nums1]
        return result
