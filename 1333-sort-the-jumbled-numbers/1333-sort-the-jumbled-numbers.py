class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        hm = defaultdict(list)
        for i, num in enumerate(nums):
            cur = 0
            for d in str(num):
                cur = cur * 10 + mapping[int(d)]
            hm[cur].append(num)
        hm = sorted(hm.items(), key=lambda x: (x[0]))
        ans = []
        for k, v in hm:
            ans.extend(v)
        return ans
