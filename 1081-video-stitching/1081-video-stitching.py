class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # https://algo.monster/liteproblems/1024  similar to frog jump
        # Initialize a list to keep track of the furthest point each second can reach
        target_time = time
        furthest_reach = [0] * target_time
      
        # Pre-process the clips to fill in the furthest_reach list
        for start, end in clips:
            # Only consider clips that start before the target_time
            if start < target_time:
                # Update the furthest_reach for the second that this clip starts
                furthest_reach[start] = max(furthest_reach[start], end)
      
        clips_required = 0  # Counter for the minimum number of clips required
        current_end = 0     # The furthest point we can reach without adding another clip
        next_end = 0        # The furthest point we can reach by including another clip
      
        # Iterate through each second up to the target_time
        for second in range(target_time):
            # Determine the most distant point in time we can reach from this second
            next_end = max(next_end, furthest_reach[second])
          
            # If the next_end is less or equal to the current second, it means we have a gap.
            # We can't reach the current second from any previous clips.
            if next_end <= second:
                return -1
          
            # When the current second reaches the current_end, we need to select a new clip
            if current_end == second:
                clips_required += 1
                # Update current_end to the furthest point reachable from this clip
                current_end = next_end

        return clips_required


        # clips.sort()
        
        # # Initialize an array to store the minimum number of clips needed to cover each time point
        # dp = [float('inf')] * (time + 1)
        
        # # Base case: 0 clips are needed to cover time 0
        # dp[0] = 0
        
        # for clip in clips:
        #     start, end = clip
        #     for t in range(start, min(end, time) + 1):
        #         dp[t] = min(dp[t], dp[start] + 1)

        # # If dp[time] is still infinite, it means it's impossible to cover the entire time range
        # return -1 if dp[time] == float('inf') else dp[time]
        
        @cache
        def dp(i, covered, cnt):
            if covered >= time:
                ans[0] = min(ans[0], cnt)
                return
            for j in range(i + 1, n):
                if i == -1:
                    if clips[j][0] == 0:
                        dp(j, clips[j][1], cnt + 1)
                    continue
                if clips[i][1] >= clips[j][0]:
                    dp(j, clips[j][1], cnt + 1)
                else:
                    break
                # if clips[j][0] > covered:
                #     break
                # dp(j, clips[j][1], cnt + 1)

        n = len(clips)
        ans = [float('inf')] 
        clips.sort(key=lambda x: x[0])
        dp(-1, 0, 0)
        return ans[0] if ans[0] != float('inf') else -1


        @cache
        def dp(i, covered, cnt):
            if covered >= time:
                ans[0] = min(ans[0], cnt)
                return
            if i >= n:
                return

            for j in range(i + 1, n):
                if clips[j][0] > covered:
                    break
                dp(j, max(covered, clips[j][1]), cnt + 1)

        n = len(clips)
        ans = [float('inf')]
        clips.sort(key=lambda x: x[0])
        dp(-1, 0, 0)
        return ans[0] if ans[0] != float('inf') else -1