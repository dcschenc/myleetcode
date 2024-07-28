from collections import defaultdict
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hm = defaultdict(int)
        n = len(rectangles)
        for w, h in rectangles:
            hm[w/h] += 1
        cnt = 0
        for k, v in hm.items():
            cnt += v * (v - 1)//2
        return cnt
        
        