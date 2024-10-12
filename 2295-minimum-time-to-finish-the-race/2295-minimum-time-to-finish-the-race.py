class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # https://algo.monster/liteproblems/2188
        
        # # Initialize the minimum cost for each number of laps up to 17
        # # These values represent the minimum time to complete a given number of laps without changing tires
        # change_time, num_laps = changeTime, numLaps
        # min_cost_for_laps = [inf] * 18
      
        # # Calculate the minimum time to complete successive laps with each tire configuration
        # for base_time, decay_factor in tires:
        #     lap_count, current_cost, time_for_next_lap = 1, 0, base_time
        #     # Continue if the time to complete the next lap is less than or equal to the time it takes to change the tire plus the base time
        #     while time_for_next_lap <= change_time + base_time:
        #         current_cost += time_for_next_lap
        #         min_cost_for_laps[lap_count] = min(min_cost_for_laps[lap_count], current_cost)
        #         # Increase the time for the next lap by the decay factor, and increment lap count
        #         time_for_next_lap *= decay_factor
        #         lap_count += 1

        # # Initialize the dp array to store the minimum time to finish a certain number of laps
        # min_time_to_finish_laps = [inf] * (num_laps + 1)
        # # Set the base case where 0 laps take 0 time, minus the time for tire change as it's not needed yet
        # min_time_to_finish_laps[0] = -change_time
      
        # # Calculate the minimum time to complete i laps
        # for lap_i in range(1, num_laps + 1):
        #     # Consider all possible numbers of laps one could run before changing tires,
        #     # but it is not worth considering more laps than the tire can handle before decaying, hence the min(18, lap_i + 1) limit
        #     for consecutive_laps_with_one_tire in range(1, min(18, lap_i + 1)):
        #         min_time_to_finish_laps[lap_i] = min(
        #             min_time_to_finish_laps[lap_i],
        #             min_time_to_finish_laps[lap_i - consecutive_laps_with_one_tire] + min_cost_for_laps[consecutive_laps_with_one_tire]
        #         )
        #     # Add the change time for each tire switch
        #     min_time_to_finish_laps[lap_i] += change_time
      
        # # Return the minimum time to finish all the laps
        # return min_time_to_finish_laps[num_laps]


        cost = [inf] * 18
        for f, r in tires:
            i, s, t = 1, 0, f
            while t <= changeTime + f:
                s += t
                cost[i] = min(cost[i], s)
                t *= r
                i += 1
        f = [inf] * (numLaps + 1)
        f[0] = -changeTime
        for i in range(1, numLaps + 1):
            for j in range(1, min(18, i + 1)):
                f[i] = min(f[i], f[i - j] + cost[j])
            f[i] += changeTime
        return f[numLaps]
