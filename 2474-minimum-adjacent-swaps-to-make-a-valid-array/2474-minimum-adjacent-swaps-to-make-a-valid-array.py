class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2340.Minimum%20Adjacent%20Swaps%20to%20Make%20a%20Valid%20Array
        mx, mx_idx, mi, mi_idx = 0, 0, float('inf'), 0
        n, ans = len(nums), 0
        for i in range(n):
            if mx <= nums[i]:
                mx = nums[i]
                mx_idx = i
            if mi > nums[i]:
                mi = nums[i]
                mi_idx = i
        # print(mx, mx_idx, mi, mi_idx)
        ans = n - 1 - mx_idx
        if mi_idx <= mx_idx:
            return ans + mi_idx
        else:
            return ans + mi_idx - 1
