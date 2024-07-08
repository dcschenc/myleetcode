class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:        
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1130.Minimum%20Cost%20Tree%20From%20Leaf%20Values
        @cache
        def dp(i, j):
            if i == j:
                return 0           
            mi = float('inf')
            for k in range(i, j):
                left_max = max(arr[i:k+1])
                right_max = max(arr[k+1:j+1])
                cur = left_max * right_max + dp(i, k) + dp(k+1, j)
                mi = min(mi, cur)
            return mi

        return dp(0, len(arr)-1)

        # def dp(i, j):
        #     if i + 1 == j:
        #         return arr[i] * arr[j]
        #     mi = 0
        #     for k in range(i, j + 1):
        #         if k == i:
        #             cur = arr[i] * max(arr[k+1:]) + dp(i, k) + dp(k + 1, j)
        #         elif k == j :
        #             cur = max(arr[i:k+1]) * arr[j] + dp(i, k) + dp(k + 1, j)
        #         else:
        #             cur = max(arr[i:k+1]) * max(arr[k+1:]) + dp(i, k) + dp(k+1, j)
        #         mi = min(mi, cur)
        #     return mi

        # return dp(0, len(arr)-1)
        