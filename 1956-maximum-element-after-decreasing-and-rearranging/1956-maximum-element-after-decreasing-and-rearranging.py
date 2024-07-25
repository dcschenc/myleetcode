class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:    
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1846.Maximum%20Element%20After%20Decreasing%20and%20Rearranging  
        arr.sort()
        for i in range(len(arr)):
            if i == 0:
                arr[i] = 1
            if arr[i] >= arr[i-1] + 1:
                arr[i] = arr[i-1] + 1
        return arr[-1]
