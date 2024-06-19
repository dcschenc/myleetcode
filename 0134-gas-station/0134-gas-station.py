class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        total_gas, current_gas, start_station = 0, 0, 0
        for station in range(len(gas)):
            gas_diff = gas[station] - cost[station]
            total_gas += gas_diff
            current_gas += gas_diff

            if current_gas < 0:
                current_gas = 0
                start_station = station + 1   # the previous stations are not suitable as start, there are more gas in the right

        return start_station if total_gas >= 0 else -1
        
        # # Calculate the net gas available at each station (gas - cost)
        # net_gas = [g - c for g, c in zip(gas, cost)]
        
        # # If the total net gas available is negative, there is no solution
        # if sum(net_gas) < 0:
        #     return -1
        
        # # Starting from the first station, check if a full circuit can be completed
        # tank = 0
        # start = 0
        # for i, g in enumerate(net_gas):
        #     tank += g
        #     if tank < 0:
        #         # If the tank becomes negative, reset it and start from the next station
        #         tank = 0
        #         start = i + 1
        
        # # If the loop completes without returning, the starting station is valid
        # return start


        # n = len(gas)
        # start = -1
        # tank = 0
        # bal = [0] * n
        # for i in range(n):
        #     bal[i] = gas[i] - cost[i]
        # if sum(bal) < 0:
        #     return -1
        # # print(bal)
        # for i in range(n):
        #     start = i
        #     j = i  
        #     if gas[i] <=0:
        #         continue
        #     tank = bal[i]
            
        #     while tank >= 0:
        #         if j == n-1:
        #             j = 0
        #         else:
        #             j += 1                    
        #         if j == start:
        #             return start          
        #         tank += bal[j]
        #         # print(j, start, tank)          
                       
        # return -1    
        # n = len(gas)
        # start = -1
        # tank = 0
        # print(n)
        # for i in range(n):
        #     start = i
        #     tank = gas[i]
        #     while True:
        #         if tank >= cost[i]:
        #             print(i, start)
        #             j = i+1
        #             if j > n-1:
        #                 j = 0
        #             tank = tank - cost[i] + gas[j]
        #             # print(i, start)
        #             if i == n-1:
        #                 i=0
        #             else:
        #                 i += 1                    
        #             if i == start:
        #                 return i                    
        #         else:
        #             break           
        # return -1
