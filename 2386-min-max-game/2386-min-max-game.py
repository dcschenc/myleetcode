class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            i, n = 0, len(nums)
            new = []
            mi = True
            while i < n - 1:
                if mi:
                    new.append(min(nums[i], nums[i+1]))
                else:
                    new.append(max(nums[i], nums[i+1]))
                i += 2
                mi = not mi
            nums = new
        return nums[0]