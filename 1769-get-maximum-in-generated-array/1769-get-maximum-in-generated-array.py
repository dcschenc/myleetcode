class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1646.Get%20Maximum%20in%20Generated%20Array
        if n < 2:
            return n
        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i >> 1] if i % 2 == 0 else nums[i >> 1] + nums[(i >> 1) + 1]
        return max(nums)
        
        if n == 0:
            return 0        
        nums = [0] * (n+1)
        nums[0], nums[1] = 0, 1
        i = 1
        while i <= n//2:
            nums[2*i] = nums[i]
            if 2*i + 1 < n + 1:
                nums[2*i + 1] = nums[i] + nums[i+1]
            i += 1
        return max(nums)