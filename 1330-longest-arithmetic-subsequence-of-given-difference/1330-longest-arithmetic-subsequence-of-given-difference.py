class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        for i in range(n):
            if arr[i] - difference not in dp:
                dp[arr[i]] = 1
            else:
                dp[arr[i]] = dp[arr[i] - difference] + 1
        return max(dp.values())


        hm = {}
        ans = 0
        for num in arr:
            if num - difference not in hm:
                hm[num] = 1
            else:
                hm[num] = hm[num - difference] + 1
            ans = max(ans, hm[num])
        return ans