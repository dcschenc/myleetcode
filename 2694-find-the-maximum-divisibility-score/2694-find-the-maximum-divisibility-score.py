class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx = -1
        ans = 0
        divisors.sort()
        for divisor in divisors:
            cnt = sum(num % divisor == 0 for num in nums)  
            if cnt > mx:
                mx = cnt
                ans = divisor
        return ans