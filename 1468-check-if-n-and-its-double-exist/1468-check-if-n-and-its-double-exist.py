class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = {}
        for i, val in enumerate(arr):
            if val*2 in seen or val/2 in seen:
                return True
            seen[val] = i
        return False
            