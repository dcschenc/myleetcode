class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0477.Total%20Hamming%20Distance
        ans, n = 0, len(nums)
        for i in range(32):
            a = sum(x >> i & 1 for x in nums)
            b = n - a
            ans += a * b
        return ans        