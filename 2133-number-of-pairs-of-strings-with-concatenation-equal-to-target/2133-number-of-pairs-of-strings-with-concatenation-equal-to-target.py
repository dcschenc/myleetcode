from itertools import combinations
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2023.Number%20of%20Pairs%20of%20Strings%20With%20Concatenation%20Equal%20to%20Target
        ans = 0
        for a, b in combinations(nums, 2):
            if a + b == target:
                ans += 1
            if b + a == target:
                ans += 1
        return ans
