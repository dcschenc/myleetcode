class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1802.Maximum%20Value%20at%20a%20Given%20Index%20in%20a%20Bounded%20Array
        def sum(x, cnt):
            # return (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1) * x // 2 + cnt - x        
            if x >= cnt:
                return (x + (x - cnt + 1))  * cnt // 2
            else:
                return x  * (x + 1) // 2 + (cnt - x) * 1
          
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left