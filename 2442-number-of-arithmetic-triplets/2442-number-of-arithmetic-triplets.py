class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum(b - a == diff and c - b == diff for a, b, c in combinations(nums, 3))

        s = set(nums)
        ans = 0
        for n in nums:
            if n + diff in s and n + 2 * diff in s:
                ans += 1
        return ans