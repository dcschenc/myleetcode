class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = 0
        for i, a in enumerate(nums1):
            for j, b in enumerate(nums2):
                if a % (b * k) == 0:
                    total += 1
        return total