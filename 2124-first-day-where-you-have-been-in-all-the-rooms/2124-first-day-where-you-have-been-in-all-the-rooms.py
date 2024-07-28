class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1997.First%20Day%20Where%20You%20Have%20Been%20in%20All%20the%20Rooms
 
        n = len(nextVisit)
        dp = [0] * n
        mod = 10**9 + 7
        for i in range(1, n):
            dp[i] = dp[i - 1] + 1 + dp[i - 1] - dp[nextVisit[i - 1]] + 1 
            dp[i] = dp[i] % mod
        return dp[n-1] % mod


        # n = len(nextVisit)
        # days = 0
        # visited = [0] * n
        # visited[0] = 1
        # cur = 0
        # while any(v == 0 for v in visited):
        #     if visited[cur] % 2 == 1:
        #         cur = nextVisit[cur]
        #     else:
        #         cur = (cur + 1) % n
        #     visited[cur] += 1
        #     days += 1

        # return days % (10 ** 9 + 7)