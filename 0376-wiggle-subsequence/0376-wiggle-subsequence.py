class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[j] > nums[i]:
                    down[i] = max(down[i], up[j] + 1)
            ans = max(ans, up[i], down[i])
        return ans
