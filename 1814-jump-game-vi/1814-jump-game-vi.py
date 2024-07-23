from heapq import heappush, heappop
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:  
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1696.Jump%20Game%20VI
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        queue = deque([0])  # 单调队列
        for i in range(1, n):
            if i - queue[0] > k:
                queue.popleft()
            j = queue[0]
            dp[i] = max(dp[i], dp[j] + nums[i])
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            queue.append(i)
        # print(dp)
        return dp[n-1]
        

        # n = len(nums)
        # dp = [float('-inf')] * n
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     for j in range(max(0, i-k), i):
        #         dp[i] = max(dp[i], dp[j] + nums[i])
        # # print(dp)
        # return dp[n-1]
        