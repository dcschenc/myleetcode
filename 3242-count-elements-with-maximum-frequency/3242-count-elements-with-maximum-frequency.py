class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = counter.most_common()[0][1]
        return sum([v for v in counter.values() if v == mx])
        # ans = 0
        # for v in counter.values():
            
        #     if v == mx:
        #         ans += v
        # return ans