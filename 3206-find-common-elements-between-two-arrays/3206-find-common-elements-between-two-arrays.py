class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        a = b = 0
        for num in nums1:
            if num in set2:
                a += 1
        for num in nums2:
            if num in set1:
                b += 1
        return [a, b]