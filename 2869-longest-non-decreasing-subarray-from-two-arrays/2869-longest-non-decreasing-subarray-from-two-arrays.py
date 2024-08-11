class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2771.Longest%20Non-decreasing%20Subarray%20From%20Two%20Arrays
        ans = dp1 = dp2 = 1
        for i in range(1, len(nums1)):
            r11 = dp1+1 if nums1[i-1]<=nums1[i] else 1
            r21 = dp2+1 if nums2[i-1]<=nums1[i] else 1
            
            r12 = dp1+1 if nums1[i-1]<=nums2[i] else 1            
            r22 = dp2+1 if nums2[i-1]<=nums2[i] else 1
            dp1 = max(r11, r21)
            dp2 = max(r12, r22)
            ans = max(ans, dp1, dp2)
        return ans
