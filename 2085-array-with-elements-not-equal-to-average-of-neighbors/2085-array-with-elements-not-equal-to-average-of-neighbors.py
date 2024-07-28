class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        i, mid = 0, n // 2 + 1
        ans = []
        while i < mid:
            ans.append(nums[i])
            if i + mid < n:
                ans.append(nums[i + mid])
            i += 1
        return ans