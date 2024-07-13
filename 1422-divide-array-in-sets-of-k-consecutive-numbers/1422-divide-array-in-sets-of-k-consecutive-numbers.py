from collections import defaultdict, Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        # nums.sort()
        hm = Counter(nums)
        items = sorted(hm.keys())
        for num in items:
            if hm[num] == 0: continue
            cnt = hm[num]
            for j in range(1, k):
                if num + j not in hm or hm[num + j] < cnt:
                    return False
                hm[num + j] -= cnt
        return True
                
            
