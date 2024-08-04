class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2420.Find%20All%20Good%20Indices
        
        n = len(nums)
        prefix = [False] * n
        prefix[0] = True
        cur = 1
        for i in range(1, n):            
            cur += 1               
            if nums[i] > nums[i-1]:
                cur = 1
            if cur >= k:
                prefix[i] = True

        suffix = [False] * n
        suffix[-1] = True
        cur = 1
        for i in range(n-2, -1, -1):            
            cur += 1                
            if nums[i] > nums[i+1]:
                cur = 1
            if cur >= k:
                suffix[i] = True
        ans = []
        for i in range(k, n-k):
            if prefix[i-1] and suffix[i+1]:
                ans.append(i)
        return ans

