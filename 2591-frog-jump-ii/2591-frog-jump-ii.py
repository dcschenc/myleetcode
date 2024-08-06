class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2498.Frog%20Jump%20II
        ans = stones[1] - stones[0]
        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])
        return ans