from collections import defaultdict
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # result = 0
        # count_map = {}
        # for num in nums:
        #     if num not in count_map:
        #         count_map[num] = 1
        #     else:
        #         count_map[num] += 1
        # for num, count in count_map.items():
        #     if num + 1 in count_map:
        #         result = max(count + count_map[num + 1], result)
        # return result
        # n = len(nums)
        # hm = defaultdict(int)
        # for num in nums:
            # hm[num] += 1
        hm = Counter(nums)
        max_cnt = 0        
        # for k, v in sorted(hm.items(), key=lambda x: x[0]):
        for k, v in hm.items():
            if k+1 in hm:
                if hm[k] + hm[k+1] > max_cnt:
                    max_cnt = hm[k] + hm[k+1]
        return max_cnt

