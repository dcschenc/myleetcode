class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        # Try removing 3 smallest elements
        min_diff = nums[-1] - nums[3]
        
        # Try removing 3 largest elements
        min_diff = min(min_diff, nums[n-4] - nums[0])
        
        # Try removing 2 smallest and 1 largest elements
        min_diff = min(min_diff, nums[n-3] - nums[1])
        
        # Try removing 1 smallest and 2 largest elements
        min_diff = min(min_diff, nums[n-2] - nums[2])
        
        return min_diff


        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1509.Minimum%20Difference%20Between%20Largest%20and%20Smallest%20Value%20in%20Three%20Moves
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        ans = inf
        for l in range(4):
            r = 3 - l
            ans = min(ans, nums[n - 1 - r] - nums[l])
        return ans       
   
        # low = max(nums[3:]) - min(nums[3:])
        # high = max(nums[:-3]) - min(nums[:-3])
        # return min(low, high)