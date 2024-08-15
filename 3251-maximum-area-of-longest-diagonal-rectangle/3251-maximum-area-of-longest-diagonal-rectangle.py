class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans, mx = 0, 0
        for w, h in dimensions:
            if math.sqrt(w ** 2 + h ** 2) > mx:
                mx = math.sqrt(w ** 2 + h **2)
                ans = w * h
            elif math.sqrt(w ** 2 + h ** 2) == mx and w * h > ans:
                ans = w * h
        return ans
        