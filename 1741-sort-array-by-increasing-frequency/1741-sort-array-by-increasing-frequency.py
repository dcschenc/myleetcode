from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] += 1
        sorted_items = sorted(hm.items(), key=lambda x: (x[1], -x[0]))
        result = []
        for k, v in sorted_items:
            for _ in range(v):
                result.append(k)
        return result