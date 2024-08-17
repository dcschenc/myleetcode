class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        mi1 = min(nums1)
        mi2 = min(nums2)
        return mi2 - mi1