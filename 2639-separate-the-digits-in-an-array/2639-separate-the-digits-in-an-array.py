class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            for d in str(n):
                ans.append(int(d))
        return ans