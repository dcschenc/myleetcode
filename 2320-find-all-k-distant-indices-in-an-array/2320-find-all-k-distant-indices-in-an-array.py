class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     if any(abs(i - j) <= k and nums[j] == key for j in range(n)):
        #         ans.append(i)
        # return ans

        n = len(nums)
        target = [i for i, num in enumerate(nums) if num == key]        
        ans = []
        for i , num in enumerate(nums):
            idx = bisect_left(target, i)
            if idx > 0 and target[idx-1] + k >= i or idx < len(target) and target[idx] - i <= k:
                ans.append(i)
        return ans