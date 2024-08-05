class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] <<= 1
                nums[i + 1] = 0
        ans = [0] * n
        i = 0
        for x in nums:
            if x:
                ans[i] = x
                i += 1
        return ans

        
        n, i = len(nums), 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i += 1
        ans = []
        for num in nums:
            if num:
                ans.append(num)
        return ans + [0] * (len(nums) - len(ans))