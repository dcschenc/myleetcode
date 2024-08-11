class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2780.Minimum%20Index%20of%20a%20Valid%20Split
        n = len(nums)
        t, c = Counter(nums).most_common()[0]
        cur = 0
        for i in range(len(nums)):
            if nums[i] == t:
                cur += 1
            if cur * 2 > i + 1 and (c - cur) * 2 > (n - i - 1):
                return i
        return -1
