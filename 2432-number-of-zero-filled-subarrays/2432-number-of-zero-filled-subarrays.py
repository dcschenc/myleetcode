class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2348.Number%20of%20Zero-Filled%20Subarrays/
        ans = cnt = 0
        for v in nums:
            cnt = 0 if v else cnt + 1
            ans += cnt
        return ans
                
        i, n = 0, len(nums)
        cnt = 0
        while i < n:
            while i < n and nums[i] != 0:
                i += 1
            j = i
            while j < n and nums[j] == 0:
                j += 1            
            cnt += (j-i)*(j-i+1)//2
            i = j
        return cnt
