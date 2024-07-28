class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:  
        # Calculate the number of tasks.
        num_tasks = len(tasks)
      
        # Initialize a list of booleans to keep track of which combinations of tasks
        # can fit into a single session.
        can_fit_session = [False] * (1 << num_tasks)
      
        # Check all combinations of tasks.
        for mask in range(1, 1 << num_tasks):
            # Calculate the total time of tasks in the current combination.
            total_time = sum(tasks[j] for j in range(num_tasks) if mask >> j & 1)
          
            # Set True in can_fit_session if the total time of tasks is within the sessionTime.
            can_fit_session[mask] = total_time <= sessionTime
      
        # Initialize an array to store the minimum sessions needed for every task combination.
        min_sessions_needed = [inf] * (1 << num_tasks)
        # Base case: zero tasks require zero sessions.
        min_sessions_needed[0] = 0

        # Calculate the minimum sessions required for all the combinations.
        for mask in range(1, 1 << num_tasks):
            # Store the current mask to iterate over its subsets.
            subset = mask
            # Iterate over all the subsets of the mask.
            while subset:
                # Check if the current subset can fit into one session.
                if can_fit_session[subset]:
                    # Update the minimum sessions needed if we can achieve a smaller number.
                    min_sessions_needed[mask] = min(min_sessions_needed[mask], min_sessions_needed[mask ^ subset] + 1)
                # Move to the next subset.
                subset = (subset - 1) & mask
      
        # Return the minimum sessions needed for all tasks.
        return min_sessions_needed[-1]

        def backtrack(idx):
            nonlocal ans           
            if len(combo) >= ans:
                return
            if idx == len(tasks):
                ans = min(ans, len(combo))
                return
            for i in range(len(combo)):
                if tasks[idx] + combo[i] <= sessionTime:
                    combo[i] += tasks[idx]
                    backtrack(idx + 1)
                    combo[i] -= tasks[idx]
            combo.append(tasks[idx])
            backtrack(idx + 1)
            combo.pop()
        
        ans = len(tasks)
        combo = []        
        tasks.sort(reverse=True)
        backtrack(0)
        return ans


        subsets = []
        self.ans = len(tasks)        
        def func(idx):
            if len(subsets) >= self.ans:
                return
            
            if idx == len(tasks):
                self.ans = min(self.ans, len(subsets))
                return
            
            for i in range(len(subsets)):
                if subsets[i] + tasks[idx] <= sessionTime:
                    subsets[i] += tasks[idx]
                    print(subsets, 'inner')
                    func(idx + 1)
                    subsets[i] -= tasks[idx]
            print(subsets)
            subsets.append(tasks[idx])
            func(idx + 1)
            subsets.pop()
        
        func(0)
        return self.ans

        tasks.sort(reverse=True)        
        n = len(tasks)
        visited = [False] * n        
        i, cnt = 0, 0
        print(tasks)
        while i < n:            
            # k = i            
            if visited[i] is True:
                i += 1
                continue
            time = 0
            for k in range(i, n):
                if visited[k] is False and time + tasks[k] <= sessionTime:
                    time += tasks[k]
                    visited[k] = True
            print(visited)
            if time == 0:
                break
            cnt += 1
            i += 1
        return cnt

        # tasks.sort(reverse=True)
        # n = len(tasks)
        # i, j = 0, n - 1
        # cnt = 0
        # # print(tasks)
        # while i <= j:            
        #     k = i            
        #     time = 0
        #     while k <= j and time + tasks[k] <= sessionTime:
        #         time += tasks[k]
        #         k += 1
        #     while j >= k and time + tasks[j] <= sessionTime:
        #         time += tasks[j]
        #         j -= 1
        #     # print(k, j, time)
        #     cnt += 1
        #     i = k
        # return cnt