class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1425.Constrained%20Subsequence%20Sum
        n = len(nums)
        dp = nums[:]  # dp[i] starts as nums[i]
        queue = deque()  # This will store indices
        
        for i in range(n):
            # Remove elements from the queue that are out of the current window
            if queue and queue[0] < i - k:
                queue.popleft()
            
            # If queue is not empty, update dp[i] with the maximum sum we can get by extending any of the last k elements
            if queue:
                dp[i] = max(dp[i], nums[i] + dp[queue[0]])
            
            # Remove elements from the queue that are smaller than the current dp[i]
            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()
            
            # Add current index to the queue
            queue.append(i)
        
        return max(dp)