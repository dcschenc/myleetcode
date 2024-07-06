class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # https://leetcode.com/problems/two-city-scheduling/editorial/
        
        # Sort by a gain which company has 
        # by sending a person to city A and not to city B
        costs.sort(key = lambda x : x[0] - x[1])
        
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total


        # diff = [-b + a for a, b in costs]
        # diff.sort()
        # deduct = 0
        # for i in range(len(costs)//2):
        #     deduct += diff[i]
        # total = sum([b for a, b in costs])
        # return total + deduct