class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1094.Car%20Pooling
        
        # Initialize an array to represent the capacity at each stop (0 to 1000)
        stops_capacity = [0] * 1001
        
        for trip in trips:
            passengers, start, end = trip
            # Decrease capacity at pickup location
            stops_capacity[start] += passengers
            # Increase capacity at drop-off location
            stops_capacity[end] -= passengers

        current_capacity = 0
        for capacity_change in stops_capacity:
            current_capacity += capacity_change
            # Check if the car's capacity is exceeded at any stop
            if current_capacity > capacity:
                return False

        return True

        ## RC ##
        ## APPROACH : GREEDY ##
        ## Similar To Leetcode : 253. Meeting Rooms II ##
        """
        1. Similar to Meetings Rooms II, we sort start and end timings, but here we also maintain number of passengers getting in  and number of passengers getting out. tuple => ( start/end time, passengers in/out )
        2. We keep on adding passengers, until we reach one end point (i.e if start < end)
        3. At any moment if passengers are more than capacity we return False
        4. When we reach end point, we decrement passengers and continue.
        
        Example : [[8,2,3],[4,1,3],[1,3,6],[8,4,6],[4,4,8]]
        Capacity : 12
        STACK TRACE : passengers, start pointer time, end pointer time
                        4       2   3
                        12      3   3
                        1       4   6
                        5       4   6
        Ans : False
        """

        start_timings = sorted( [(trip[1], trip[0]) for trip in trips] )
        end_timings = sorted( [(trip[2], trip[0]) for trip in trips] )

        passengers = 0
        start = end = 0
        while( start < len(trips) ):
            if start_timings[start][0] < end_timings[end][0]:
                passengers += start_timings[start][1]
            else:
                passengers -= end_timings[end][1]
                end += 1
                continue    # watchout
            start += 1

            if passengers > capacity:
                return False
            # print(passengers, start_timings[start][0], end_timings[end][0])
        return True

        # trips.sort(key=lambda x: x[1])
        # print(trips)
        # cur = capacity - trips[0][0]
        # if cur < 0: return False
        # end = trips[0][2]
        # last_t = 0
        # for i in range(1, len(trips)):                 

        #     if end <= trips[i][1]:
        #         while last_t <= i-1 and end <=trips[i][1]:
        #             cur = cur + trips[last_t][0]
        #             last_t += 1
        #             end = trips[last_t][2]
        #         # cur = capacity - trips[i][0]                
        #     else:
        #         cur -= trips[i][0]            
        #     print(cur, i)
        #     if cur < 0:
        #         return False
        #     if trips[i][2] < end:
        #         cur += trips[i][0]
        # return True
