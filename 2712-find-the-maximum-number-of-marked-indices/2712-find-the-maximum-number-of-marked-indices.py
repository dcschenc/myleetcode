class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2576.Find%20the%20Maximum%20Number%20of%20Marked%20Indices
        nums.sort()
        n = len(nums)
        i, j = 0, (n + 1) // 2
        ans = 0
        while j < n:
            while j < n and nums[i] * 2 > nums[j]:
                j += 1
            if j < n:
                ans += 2
            i, j = i + 1, j + 1
        return ans