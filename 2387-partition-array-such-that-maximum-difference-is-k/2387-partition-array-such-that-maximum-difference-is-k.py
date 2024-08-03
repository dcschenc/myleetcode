class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i, n = 0, len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j+1] - nums[i] <= k:
                j += 1
            cnt += 1
            i = j + 1
        return cnt