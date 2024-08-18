class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3152.Special%20Array%20II
        n = len(nums)
        d = list(range(n))
        for i in range(1, n):
            if nums[i] % 2 != nums[i - 1] % 2:
                d[i] = d[i - 1]
        return [d[t] <= f for f, t in queries]