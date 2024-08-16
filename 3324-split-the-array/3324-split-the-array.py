class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for val in counter.values():
            if val > 2:
                return False
        return True