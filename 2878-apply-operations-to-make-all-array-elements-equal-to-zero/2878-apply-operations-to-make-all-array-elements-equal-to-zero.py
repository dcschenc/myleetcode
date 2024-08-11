class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2772.Apply%20Operations%20to%20Make%20All%20Array%20Elements%20Equal%20to%20Zero
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = [0] * (n + 1)
        s = 0
        for i, x in enumerate(nums):
            s += d[i]
            x += s
            if x == 0:
                continue
            if x < 0 or i + k > n:
                return False
            s -= x
            d[i + k] += x
        return True
        
        n = len(nums)
        deltas = [0] * n
        decreased = 0
        for i in range(n):
            decreased -= deltas[i] # Remove the outdated window
            actual = nums[i] - decreased 
            if actual < 0 or (actual > 0 and i + k - 1 >= n):
                return False
            decreased += actual
            if i + k < n:
                deltas[i + k] += actual
        return True       
        
        # i, n = 0, len(nums)
        # while i <= n - k:
        #     if nums[i] < 0:
        #         return False
        #     if nums[i] != 0:
        #         tmp = nums[i]
        #         for j in range(i, i+k):
        #             nums[j] -= tmp            
        #     i += 1
        # for i in range(n-k, n):
        #     if nums[i] != 0:
        #         return False
        # return True
            