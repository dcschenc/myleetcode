class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1186.Maximum%20Subarray%20Sum%20with%20One%20Deletion
        n = len(arr)
        left = [0] * n
        right = [0] * n
        total = 0
        for i, x in enumerate(arr):
            total = max(total, 0) + x
            left[i] = total
        total = 0
        for i in range(n - 1, -1, -1):
            total = max(total, 0) + arr[i]
            right[i] = total
            
        ans = max(left)
        for i in range(1, n - 1):
            ans = max(ans, left[i - 1] + right[i + 1])
        return ans

        # n = len(arr)
        # prefix = [0] * n
        # prev = prefix[0] = arr[0]
        # for i in range(1, n):
        #     if prev < 0:
        #         prev = arr[i]
        #     else:
        #         prev += arr[i]
        #     prefix[i] = prev
        # postfix = [0] * n
        # prev = postfix[n-1] = arr[-1]
        # for i in range(n-2, -1, -1):
        #     if prev < 0:
        #         prev = arr[i]
        #     else:
        #         prev += arr[i]
        #     postfix[i] = prev
        # ans = -float('inf')
        # for i in range(n):
        #     if i > 0 and i < n - 1:
        #         if arr[i] < 0:
        #             ans = max(ans, prefix[i-1] + postfix[i+1])
        #         else:
        #             ans = max(ans, prefix[i-1] + postfix[i+1] + arr[i])
        #     ans = max(ans, prefix[i])
        #     ans = max(ans, postfix[i])

        # return ans