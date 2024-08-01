class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = Counter()
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] == key:
                counter[nums[i]] += 1
        return counter.most_common(1)[0][0]