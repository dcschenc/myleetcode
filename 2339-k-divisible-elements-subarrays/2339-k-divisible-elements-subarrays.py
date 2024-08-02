class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2261.K%20Divisible%20Elements%20Subarrays
        n = len(nums)
        hm = set()
        for i in range(n):            
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k: 
                    break
                hm.add(tuple(nums[i:j+1]))
        return len(hm)

      
