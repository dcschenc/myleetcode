class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Number of friends (or chairs needed)
        num_friends = len(times)
      
        # Initialize the heaps for available chairs and chairs currently taken
        available_chairs = list(range(num_friends))
        heapq.heapify(available_chairs)
        occupied_chairs = []
      
        # Add the friend's index to each arrival and leaving time
        for friend_index in range(num_friends):
            times[friend_index].append(friend_index)
      
        # Sort the times based on arrival times
        times.sort()
      
        # Iterate over each friend's time
        for arrival, departure, friend_index in times:
            # Free up chairs if current time is past the departure time of any friend
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                chair_num = heapq.heappop(occupied_chairs)[1]
                heapq.heappush(available_chairs, chair_num)
          
            # Assign the smallest available chair to the current friend
            current_chair = heapq.heappop(available_chairs)
          
            # If the current friend is the target friend, return the chair number
            if friend_index == targetFriend:
                return current_chair
          
            # Mark the chair as occupied until departure
            heapq.heappush(occupied_chairs, (departure, current_chair))

        # If the target friend's chair was not found, return -1 (though this should never happen)
        return -1
