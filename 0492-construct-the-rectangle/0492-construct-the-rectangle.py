import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        L = area
        # diff = area - 1
        mid = int(math.sqrt(area))
        L = W = mid
        while True:
            tetative = L * W
            if tetative == area:
                return [L, W]
            if tetative > area:
                W = W-1
            else:
                L = L+1
        

