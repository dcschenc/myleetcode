class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for k, v in counter.items():
            if v == 1:
                ans += k
        return ans