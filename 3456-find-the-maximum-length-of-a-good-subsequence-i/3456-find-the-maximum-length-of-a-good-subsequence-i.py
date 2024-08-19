class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3176.Find%20the%20Maximum%20Length%20of%20a%20Good%20Subsequence%20I
        n = len(nums)
        f = [[1] * (k + 1) for _ in range(n)]
        ans = 0
        for i, x in enumerate(nums):
            for h in range(k + 1):
                for j, y in enumerate(nums[:i]):
                    if x == y:
                        f[i][h] = max(f[i][h], f[j][h] + 1)
                    elif h:
                        f[i][h] = max(f[i][h], f[j][h - 1] + 1)
            ans = max(ans, f[i][k])
        return ans