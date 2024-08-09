class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        set1, set2 = set(), set()
        n = len(nums)
        ans = []
        for i in range(n):
            set1.add(nums[i])
            ans.append(len(set1))

        for i in range(n-1, -1, -1):
            ans[i] -= len(set2)
            set2.add(nums[i])

        return ans
            