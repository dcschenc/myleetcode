class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2717.Semi-Ordered%20Permutation
        n = len(nums)
        mi, mx = min(nums), max(nums)        
        mi_idx, mx_idx = nums.index(mi), nums.index(mx)
        if mi_idx < mx_idx:
            return mi_idx + (n - 1 - mx_idx)
        else:
            return mi_idx + (n - 1 - mx_idx) - 1