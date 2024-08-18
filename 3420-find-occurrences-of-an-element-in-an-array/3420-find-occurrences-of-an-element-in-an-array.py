class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        idx = []
        for i, num in enumerate(nums):
            if x == num:
                idx.append(i)
        ans, n = [], len(idx)
        for q in queries:
            if q > n:
                ans.append(-1)
            else:
                ans.append(idx[q-1])
        return ans
