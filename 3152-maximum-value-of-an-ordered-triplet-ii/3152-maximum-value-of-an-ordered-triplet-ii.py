class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2874.Maximum%20Value%20of%20an%20Ordered%20Triplet%20II
        ans = mx = mx_diff = 0
        for num in nums:
            ans = max(ans, mx_diff * num)
            mx = max(mx, num)
            mx_diff = max(mx_diff, mx - num)
        return ans