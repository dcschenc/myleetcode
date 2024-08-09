class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2717.Semi-Ordered%20Permutation
        # If 1 is to the left of n, the total moves will be the sum of both shifts.
        # If 1 is to the right of n, subtract one from the total since moving 1 left also moves n closer to its final position.
        n = len(nums)
        mi, mx = min(nums), max(nums)        
        mi_idx, mx_idx = nums.index(mi), nums.index(mx)
        if mi_idx < mx_idx:
            return mi_idx + (n - 1 - mx_idx)
        else:
            return mi_idx + (n - 1 - mx_idx) - 1