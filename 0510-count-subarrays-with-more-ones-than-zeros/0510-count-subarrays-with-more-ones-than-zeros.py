from collections import Counter
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/solutions/1554228/python3-o-n-calculate-difference-between-ones-and-zeros/
        MOD = 10 ** 9 + 7
        counts = Counter({0: 1})
        res = s = dp = 0
        for num in nums:
            if num == 1:
                s += 1
                dp += counts[s - 1]
            else:
                s -= 1
                dp -= counts[s]
            res = (res + dp) % MOD
            counts[s] += 1
        
        return res % MOD