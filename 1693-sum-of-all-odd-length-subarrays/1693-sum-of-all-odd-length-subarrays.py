class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1588.Sum%20of%20All%20Odd%20Length%20Subarrays        
        ans, n = 0, len(arr)
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if (j - i + 1) & 1:
                    ans += s
        return ans