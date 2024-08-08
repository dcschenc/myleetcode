class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        mx = 0
        for i in range(m):
            for j in range(n):
                if (i == j or i + j == n - 1):
                    x = nums[i][j]
                    if x >= 2 and all(x % k for k in range(2, int(sqrt(x)) + 1)):
                        mx = max(mx, x)
        return mx

        