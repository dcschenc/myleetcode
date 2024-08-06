class Solution:
    def pivotInteger(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2485.Find%20the%20Pivot%20Integer
        total = n * (n + 1) // 2
        cur = 0
        for i in range(1, n + 1):
            if cur == total - cur - i:
                return i
            cur += i
        return -1