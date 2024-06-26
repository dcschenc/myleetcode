class Solution:
    # https://leetcode.com/problems/task-scheduler/solutions/3957131/explanation-of-the-greedy-solution/
    def leastInterval(self, tasks: List[str], n: int) -> int:       
        ######### method 1 heap ########
        
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        
        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            time += task_count if not pq else n + 1
        return time

        ########## method 2 greedy ######## 
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        
        # Count the tasks with the same max frequency
        max_frequency_tasks = list(task_counts.values()).count(max_frequency)
        
        # Calculate idle time
        # idle_time = (max_frequency - 1) * n
        
        # Calculate total time required
        total_time = (max_frequency - 1) * (n + 1) + max_frequency_tasks
        
        # Return the maximum of total time and the length of the tasks list
        return max(total_time, len(tasks))