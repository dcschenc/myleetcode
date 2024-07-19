class Solution:
    def minOperations(self, n: int) -> int:
        left, right = 1, 2*(n-1) + 1
        ans = 0
        while left < right:
            ans += (right - left) // 2
            left += 2
            right -= 2
        return ans