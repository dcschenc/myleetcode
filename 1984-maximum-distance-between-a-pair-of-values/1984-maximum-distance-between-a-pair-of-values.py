class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1855.Maximum%20Distance%20Between%20a%20Pair%20of%20Values
        ans = 0
        nums2 = nums2[::-1]
        for i, v in enumerate(nums1):
            j = len(nums2) - bisect_left(nums2, v) - 1
            ans = max(ans, j - i)
        return ans

        ans = 0
        m, n = len(nums1), len(nums2)
        for i in range(m):
            x = nums1[i]
            left, right = i, n-1
            while left <= right:
                mid = (left + right) // 2
                if nums2[mid] >= nums1[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            ans = max(ans, left - 1 - i)
        return ans