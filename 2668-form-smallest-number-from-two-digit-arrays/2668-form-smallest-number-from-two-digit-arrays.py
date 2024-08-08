class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if set(nums1) & set(nums2):
            return min(set(nums1) & set(nums2))
        else:
            return min(nums1[0], nums2[0]) * 10 + max(nums1[0], nums2[0])