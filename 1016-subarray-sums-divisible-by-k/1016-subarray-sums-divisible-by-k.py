class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = accumulate(nums, initial = 0)
        hm, ans = defaultdict(list), 0
        for i, s in enumerate(pre):
            if i == 0: continue
            mod = s % k
            if mod in hm:
                ans += len(hm[mod])
            if mod == 0:
                ans += 1            
            hm[mod].append(i)
        return ans