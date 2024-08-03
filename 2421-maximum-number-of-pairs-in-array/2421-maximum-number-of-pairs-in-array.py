class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        pairs = sum([p // 2 for p in counter.values()])
        return [pairs, n - 2 * pairs]
