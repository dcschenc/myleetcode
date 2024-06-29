class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [defaultdict(int) for i in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(i):
                next_key = arr[i] + arr[j]
                if arr[i] not in dp[j]:
                    dp[i][next_key] = max(dp[i][next_key], 2)                    
                else:
                    dp[i][next_key] = max(dp[i][next_key], dp[j][arr[i]] + 1)
                max_len = max(max_len, dp[i][next_key])

        return max_len if max_len > 2 else 0
        