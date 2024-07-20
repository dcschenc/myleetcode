class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1578.Minimum%20Time%20to%20Make%20Rope%20Colorful

        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0
        
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0
            
            # Find all the balloons having the same color as the 
            # balloon indexed at i, record the total removal time 
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            
            # Once we reach the end of the current group, add the cost of 
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j
        
        return total_time
        
        ans = 0
        cur = 0
        max_time = neededTime[0]
        pre_sum = neededTime[0]
        for i in range(1, len(colors)):
            if colors[i] == colors[cur]:
                max_time = max(max_time, neededTime[i])
                pre_sum +=  neededTime[i]
                if i == len(colors) - 1:
                    if i - cur >= 1:
                        ans += (pre_sum - max_time)
            else:
                if i - cur > 1:
                    ans += (pre_sum - max_time)
                pre_sum = max_time = neededTime[i]
                cur = i
        return ans

