class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            start_time, _, cur_profit = jobs[i-1]
            j = bisect_right(jobs, start_time, hi = i - 1, key=lambda x:x[1])
            dp[i] = max(dp[i-1], cur_profit + dp[j])
        return dp[n]

        
        # Combine and sort jobs by their end times
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        n = len(jobs)
        
        # Initialize DP array
        dp = [0] * (n + 1)
        
        # Extract individual start times for bisect_right usage
        end_times = [job[1] for job in jobs]
        
        # Dynamic Programming loop
        for i in range(1, n + 1):
            start_time, end_time, cur_profit = jobs[i-1]
            # Find the latest job that ends before the current job starts
            j = bisect_right(end_times, start_time)
            # Update DP array
            dp[i] = max(dp[i-1], cur_profit + dp[j])
        
        return dp[n]

        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])
        n = len(jobs)
        dp = [0] * (n + 1)
        for i in range(n-1, -1, -1):
            _, endTime, cur_profit = jobs[i] 
            j = bisect_left(jobs, endTime, lo = i + 1, key = lambda x: x[0])
            # either skipping the current job or taking the current job and adding its profit to the profit of the next non-overlapping job
            dp[i] = max(dp[i+1], cur_profit + dp[j])
        return dp[0] 


        @cache
        def dfs(i):
            if i >= n:
               return 0
            _, endTime, cur_profit = jobs[i] 
            j = bisect_left(jobs, endTime, lo = i + 1, key = lambda x: x[0])
            return max(dfs(i + 1), cur_profit + dfs(j))

        n = len(startTime)
        jobs = sorted(zip(startTime, endTime, profit), key = lambda x: x[0])     
        return dfs(0)
