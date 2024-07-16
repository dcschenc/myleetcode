from collections import Counter
class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = Counter(arr)
        cnt = 0
        for k, v in counter.items():
            if k + 1 in counter:
                cnt += v
        return cnt