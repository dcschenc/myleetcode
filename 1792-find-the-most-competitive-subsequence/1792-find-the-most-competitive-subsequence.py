class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1673.Find%20the%20Most%20Competitive%20Subsequence
        stk, n = [], len(nums)
        for i in range(n):
            while stk and stk[-1] > nums[i] and len(stk) + (n - i) > k:
                stk.pop()
            if len(stk) < k:
                stk.append(nums[i])
        return stk