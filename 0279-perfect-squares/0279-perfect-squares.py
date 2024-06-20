from collections import deque

class Solution:
   
    def numSquares(self, n: int) -> int:
        if n == int(sqrt(n)) ** 2:
            return 1
        dp = [float(inf)] * (n+1)
        step = int(sqrt(n))
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(int(sqrt(n)) + 1):
                dp[i] = min(dp[i], dp[i - j*j] + 1)
        return dp[-1]



         ######### BFS ###########
        step = int(sqrt(n))
        queue = deque([n])
        visited = {n}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                for i in range(1,step+1):
                    diff = cur - (i ** 2)
                    if diff == 0:
                        return steps + 1
                    if diff > 0 and diff not in visited:
                        visited.add(diff)
                        queue.append(diff)
            steps +=1
        return steps
            