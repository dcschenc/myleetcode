from sortedcontainers import SortedList
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3073.Maximum%20Increasing%20Triplet%20Value
        n = len(nums)
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(nums[i], right[i + 1])
        sl = SortedList([nums[0]])
        ans = 0
        for j in range(1, n - 1):
            if right[j + 1] > nums[j]:
                i = sl.bisect_left(nums[j]) - 1
                if i >= 0:
                    ans = max(ans, sl[i] - nums[j] + right[j + 1])
            sl.add(nums[j])
        return ans