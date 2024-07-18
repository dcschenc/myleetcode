from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # hm = defaultdict(int)
        # for num in nums:
        #     hm[num] += 1
        hm = Counter(nums)
        cnt = 0
        for k, v in hm.items():
            cnt += v * (v - 1)//2
        return cnt