class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3153.Sum%20of%20Digit%20Differences%20of%20All%20Pairs
        n = len(nums)
        m = int(log10(nums[0])) + 1
        ans = 0
        for _ in range(m):
            cnt = Counter()
            for i, x in enumerate(nums):
                nums[i], y = divmod(x, 10)
                cnt[y] += 1
            ans += sum(v * (n - v) for v in cnt.values()) // 2
        return ans