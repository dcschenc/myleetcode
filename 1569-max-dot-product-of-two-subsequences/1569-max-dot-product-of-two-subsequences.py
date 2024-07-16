class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1458.Max%20Dot%20Product%20of%20Two%20Subsequences
        m, n = len(nums1), len(nums2)
        dp = [[-inf] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                v = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], max(dp[i - 1][j - 1], 0) + v)
        return dp[-1][-1]
                
        # @cache
        # def dp(i, j):
        #     if i == len(nums1) or j == len(nums2):
        #         return 0
            
        #     use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
        #     return max(use, dp(i + 1, j), dp(i, j + 1))
            
        # if max(nums1) < 0 and min(nums2) > 0:
        #     return max(nums1) * min(nums2)
        
        # if min(nums1) > 0 and max(nums2) < 0:
        #     return min(nums1) * max(nums2)
        
        # return dp(0, 0)