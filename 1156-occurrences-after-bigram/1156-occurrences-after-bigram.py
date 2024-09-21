class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        arr = text.split()
        for i in range(1, len(arr)):
            if arr[i-1] == first and arr[i] == second and i+1 < len(arr):
                ans.append(arr[i+1])
        return ans