class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Sort tasks by the end time
        tasks.sort(key=lambda x: x[1])

        # Initialize a list to keep track of visited time slots, assuming the maximum end time is less than 2010
        visited = [0] * 2010

        # Initialize answer to count the minimum time required to finish all tasks
        minimum_time_required = 0

        # Iterate over each task
        for start_time, end_time, duration in tasks:
            # Decrease duration by the number of already visited time slots within the task's window
            duration -= sum(visited[start_time:end_time + 1])

            # Initialize a pointer at the end time of the current task
            i = end_time

            # Check if we can place the task in the current window and still need more duration
            while i >= start_time and duration > 0:
                # If the time slot is not yet visited
                if not visited[i]:
                    # Decrease the remaining duration since we are using this time slot
                    duration -= 1

                    # Mark this time slot as visited
                    visited[i] = 1

                    # Increment the minimum time required since we've occupied another time slot
                    minimum_time_required += 1

                # Move to the previous time slot and repeat till the start time or the task duration is met
                i -= 1

        # Return the computed minimum time required to finish all tasks
        return minimum_time_required