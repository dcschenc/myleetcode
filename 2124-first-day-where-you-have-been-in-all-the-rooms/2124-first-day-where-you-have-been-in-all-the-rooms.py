class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1997.First%20Day%20Where%20You%20Have%20Been%20in%20All%20the%20Rooms
        number_of_rooms = len(nextVisit)
      
        # Initialize an array to store the days to reach each room for the first time
        days_to_reach = [0] * number_of_rooms
      
        # Define the modulo for large number handling (to prevent integer overflow)
        mod = 10**9 + 7
      
        # Iterate over the rooms starting from the second room, as the first room's day count is zero by default
        for i in range(1, number_of_rooms):
            # Calculate number of days to reach this room for the first time
            # The formula is based on the previous room's day count and the day count at the 
            # index of the nextVisit for the previous room. We visit the current room after
            # visiting the previous room twice and once after nextVisit for the previous room.
            days_to_reach[i] = (days_to_reach[i - 1] + 1 + days_to_reach[i - 1] - days_to_reach[nextVisit[i - 1]] + 1) % mod
      
        # Return the number of days to reach the last room for the first time
        return days_to_reach[-1]


        # n = len(nextVisit)
        # days = 0
        # visited = [0] * n
        # visited[0] = 1
        # cur = 0
        # while any(v == 0 for v in visited):
        #     if visited[cur] % 2 == 1:
        #         cur = nextVisit[cur]
        #     else:
        #         cur = (cur + 1) % n
        #     visited[cur] += 1
        #     days += 1

        # return days % (10 ** 9 + 7)