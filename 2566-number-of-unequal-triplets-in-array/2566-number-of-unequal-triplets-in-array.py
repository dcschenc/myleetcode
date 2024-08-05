from itertools import combinations
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        # cnt = Counter(nums)
        # keys = cnt.keys()
        # ans = 0
        # for k1, k2, k3 in combinations(keys, 3):
        #     ans += cnt[k1] * cnt[k2] * cnt[k3]
        # return ans
        
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans += 1
        return ans