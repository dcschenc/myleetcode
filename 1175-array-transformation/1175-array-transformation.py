class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        n = len(arr)
        change = True
        while change:
            t = arr[:]
            change = False
            for i in range(1, n-1):
                if t[i-1] < t[i] and t[i] > t[i+1]:
                    arr[i] -= 1
                    change = True
                elif t[i] < t[i-1] and t[i] < t[i+1]:
                    arr[i] += 1
                    change = True
            
        return arr
             