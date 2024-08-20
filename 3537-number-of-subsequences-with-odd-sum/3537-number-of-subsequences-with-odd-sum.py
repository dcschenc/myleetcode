class Solution:
    def subsequenceCount(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3247.Number%20of%20Subsequences%20with%20Odd%20Sum
        mod = 10**9 + 7
        f = [0] * 2
        for x in nums:
            if x % 2:
                f[0], f[1] = (f[0] + f[1]) % mod, (f[0] + f[1] + 1) % mod
            else:
                f[0], f[1] = (f[0] + f[0] + 1) % mod, (f[1] + f[1]) % mod
        return f[1]