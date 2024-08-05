class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2450.Number%20of%20Distinct%20Binary%20Strings%20After%20Applying%20Operations
        n = len(s)
        return 2 ** (n - k + 1) % (10 ** 9 + 7)
        