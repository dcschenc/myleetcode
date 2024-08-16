class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = sum(nums[:2])
        i, n = 2, len(nums)
        ans = 1
        while i + 1 < n:
            if sum(nums[i:i+2]) != score:
                break
            i += 2
            ans += 1
        return ans
