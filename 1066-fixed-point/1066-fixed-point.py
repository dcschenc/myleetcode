class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, n in enumerate(arr):
            if i == n:
                return n
        return -1