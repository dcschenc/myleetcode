class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = ans = 0
        for i, v in enumerate(arr):
            mx = max(mx, v)
            if i == mx:
                ans += 1
        return ans

        
        n = len(arr)
        i, ans = 0, 0
        left, mx = 0, -1
        while i < n:
            if arr[i] > mx:
                mx = arr[i]
            if i - left  == mx - left:
                ans += 1
                # mx = arr[left]
            i += 1
        return ans