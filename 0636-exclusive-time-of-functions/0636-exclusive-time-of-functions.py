class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Initialize a list to hold the exclusive time for each function.
        exclusive_times = [0] * n

        # Use a stack to keep track of the function call hierarchy.
        call_stack = []

        # Store a pointer to the current time (initially set to an invalid time).
        current_time = -1

        # Process each log entry.
        for log in logs:
            # Split the string log into parts.
            parts = log.split(':')
          
            # The function id is the first part of the log, converted to an integer.
            function_id = int(parts[0])
          
            # The timestamp is the third part of the log, converted to an integer.
            timestamp = int(parts[2])

            # If the log entry indicates a start event:
            if parts[1] == 'start':
                # If there's an ongoing function, update its exclusive time.
                if call_stack:
                    exclusive_times[call_stack[-1]] += timestamp - current_time
              
                # Push the current function onto the stack.
                call_stack.append(function_id)
              
                # Update the current time to the new start time.
                current_time = timestamp
            else:  # Otherwise, it's an end event.
                # Pop the last function from the stack.
                function_id = call_stack.pop()
              
                # Update the exclusive time for this function.
                exclusive_times[function_id] += timestamp - current_time + 1
              
                # Update the current time to the end time + 1 since the next time unit
                # will indicate the start of the next event.
                current_time = timestamp + 1

        # Return the list of calculated exclusive times.
        return exclusive_times
