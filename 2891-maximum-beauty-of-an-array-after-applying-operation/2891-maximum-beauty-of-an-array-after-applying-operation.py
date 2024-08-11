class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, n = 0, 0, len(nums)
        ans = 0
        while right < n:            
            while nums[right] - nums[left] > 2 * k:
                left += 1            
            ans = max(ans, right - left + 1)
            right = right + 1          
        
        return ans