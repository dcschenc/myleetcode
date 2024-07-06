class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        cur = 0
        for i in range(n):
            cur <<= 1
            cur |= nums[i]
            if cur % 5 == 0:
                ans[i] = True
        return ans
