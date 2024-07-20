class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:  
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1590.Make%20Sum%20Divisible%20by%20P
        pre = accumulate(nums, initial = 0)
        total, hm = sum(nums), defaultdict(int)
        re = total % p 
        if re == 0:
            return 0
        ans = len(nums)
        for i, s in enumerate(pre):   
            cur = s % p 
            comp = (cur - re) % p
            if comp in hm:
                ans = min(ans, i - hm[comp])         
            hm[cur]  = i
        return ans if ans < len(nums) else -1