class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # Sort the buses and passengers in ascending order to process them in sequence
        buses.sort()
        passengers.sort()
      
        passenger_index = 0  # index of the current passenger in the sorted list
        # Iterate through buses to see how many passengers each can pick up
        for bus_arrival_time in buses:
            current_capacity = capacity  # Track the current bus's remaining capacity
            # Board passengers until the bus is full or no more passengers for the bus
            while current_capacity > 0 and passenger_index < len(passengers) and passengers[passenger_index] <= bus_arrival_time:
                # Load a passenger and decrease the available capacity
                current_capacity -= 1
                passenger_index += 1
      
        # Adjust the index back to the last boarded passenger
        passenger_index -= 1
      
        # Latest possible time to catch the bus is either bus's last arrival time
        # or just a minute before the last passenger boarded if the bus is full
        latest_time = buses[-1] if current_capacity > 0 else passengers[passenger_index]
      
        # If the bus is full, find the latest time by subtracting from the last boarded passenger's time,
        # making sure there's no passenger at that time already
        while passenger_index >= 0 and passengers[passenger_index] == latest_time:
            latest_time -= 1
            passenger_index -= 1
      
        # Return the latest time a passenger can catch the bus
        return latest_time