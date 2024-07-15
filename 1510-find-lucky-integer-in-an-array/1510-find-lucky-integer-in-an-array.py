from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for x, v in cnt.items():
            if x == v and ans < x:
                ans = x
        return ans
        
        count = Counter(arr)
        ans, max_feq = -1, 0
        for k, v in count.items():
            if k == v and v > max_feq:
                ans = k
                max_feq = v
        return ans
                