class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr)-1,-1,-1):
            tmp = mx
            mx = max(mx, arr[i])
            arr[i] = tmp
        return arr
        