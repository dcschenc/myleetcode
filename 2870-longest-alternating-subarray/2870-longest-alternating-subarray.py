class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n, ans = len(nums), -1
        for i in range(n):
            add = 1
            for j in range(i+1, n):
                if nums[j-1] + add != nums[j]:
                    break
                add = -1 * add
                ans = max(ans, j - i + 1)
        return ans

