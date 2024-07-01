class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [float(inf)] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):                       
            for j in range(i-1, -1, -1):
                if days[i-1] - days[j] < 1:
                    dp[i] = min(dp[i], dp[j] + costs[0])
                if days[i-1] - days[j] < 7:
                    dp[i] = min(dp[i], dp[j] + costs[1])
                if days[i-1] - days[j] < 30:
                    dp[i] = min(dp[i], dp[j] + costs[2])               
            
        # print(dp)
        return dp[-1]
