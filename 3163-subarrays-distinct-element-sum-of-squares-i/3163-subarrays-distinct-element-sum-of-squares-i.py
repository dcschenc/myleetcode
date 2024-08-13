class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2913.Subarrays%20Distinct%20Element%20Sum%20of%20Squares%20I
        n= len(nums)
        ans = 0
        for i in range(n):
            s = set()            
            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans