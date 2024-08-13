class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2918.Minimum%20Equal%20Sum%20of%20Two%20Arrays%20After%20Replacing%20Zeros
        s1 = sum(nums1) + nums1.count(0)
        s2 = sum(nums2) + nums2.count(0)
        if s1 > s2:
            return self.minSum(nums2, nums1)
        if s1 == s2:
            return s1
        return -1 if nums1.count(0) == 0 else s2


        total1, total2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)
        if total1 + zeros1 < total2 + zeros2:
            nums1, nums2 = nums2, nums1
            zeros1, zeros2 = nums1.count(0), nums2.count(0)
        elif total1 + zeros1 == total2 + zeros2:
            return total1 + zeros1
            
        total1 = sum(nums1) + zeros1
        return total1 if zeros2 != 0 and zeros2 + sum(nums2) <= total1 else -1
        