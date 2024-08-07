class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2599.Make%20the%20Prefix%20Sum%20Non-negative
        n = len(nums)
        ans, total = 0, 0
        heaps = []
        for i in range(n):
            total += nums[i]
            if nums[i] < 0:
                heappush(heaps, nums[i])
            while total < 0:
                x = heappop(heaps)
                total -= x
                ans += 1
        return ans