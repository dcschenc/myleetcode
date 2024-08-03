class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # https://leetcode.com/problems/task-scheduler-ii/
        day = defaultdict(int)
        ans = 0
        for task in tasks:
            ans += 1
            ans = max(ans, day[task])
            day[task] = ans + space + 1
        return ans

        
        last_day = {}  # Dictionary to store the last day each task type was performed
        current_day = 1  # Current day of the simulation

        for task in tasks:
            if task in last_day and current_day - last_day[task] <= space:
                # If a break is needed, update the current day to the next available day
                current_day = last_day[task] + space + 1

            # Perform the task on the current day
            last_day[task] = current_day
            current_day += 1

        return current_day - 1  # The last day is one less than the current day


        hm = {}
        i, n = 0, len(tasks)
        days = 0
        while i < n:
            if tasks[i] not in hm or hm[tasks[i]] + space <= days:                
                hm[tasks[i]] = days + space
                i += 1 
            else:
                days = hm[tasks[i]] + space
            # for k in hm:
            #     hm[k] += 1
            # days += 1
        return days