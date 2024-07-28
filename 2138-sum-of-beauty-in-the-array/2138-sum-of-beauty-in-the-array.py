class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        pre, post = [0] * n, [0] * n
        cur = nums[0]
        for i in range(n):
            if cur < nums[i]:
                cur = nums[i]
            pre[i] = cur

        cur = nums[n-1]
        for i in range(n-1, -1, -1):
            if nums[i] < cur:
                cur = nums[i]
            post[i] = cur

        ans = 0
        for i in range(1, n-1):
            if nums[i] > pre[i-1] and nums[i] < post[i+1]:
                ans += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                ans += 1
        return ans
