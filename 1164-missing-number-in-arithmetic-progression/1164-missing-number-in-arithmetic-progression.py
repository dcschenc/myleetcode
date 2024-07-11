class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1228.Missing%20Number%20In%20Arithmetic%20Progression
        return (arr[0] + arr[-1]) * (len(arr) + 1) // 2 - sum(arr)
        # diff = (arr[-1] - arr[0]) // len(arr)
        # if diff == 0:
        #     return arr[0]
            
        # n = len(arr)
        # for i in range(n-1):
        #     if arr[i] + diff != arr[i+1]:
        #         return arr[i] + diff
                 