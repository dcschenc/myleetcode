class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi = float('inf')
        res = []
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) < mi:
                mi = abs(arr[i] - arr[i-1])
                res = [[arr[i-1], arr[i]]]
            elif abs(arr[i] - arr[i-1]) == mi:               
                res.append([arr[i-1], arr[i]])             

        return res 