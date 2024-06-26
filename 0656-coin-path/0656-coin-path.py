class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:      
        @cache 
        def jump(i):
            if i == n - 1 and coins[i] >= 0:
                return coins[i]

            min_cost = float('inf')

            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[j] >= 0:
                    cost = coins[i] + jump(j)
                    if cost < min_cost:
                        min_cost = cost
                        next_jump[i] = j            
            
            return min_cost

        n = len(coins)
        next_jump = [-1] * n
        memo = [-1] * n

        min_cost = jump(0)
        if min_cost == float('inf'):
            return []

        res = []
        i = 0
        while i < n and next_jump[i] > 0:
            res.append(i + 1)
            i = next_jump[i]

        if i == n - 1 and coins[i] >= 0:
            res.append(n)
        else:
            return []

        return res



        # If the last coin is not accessible, no path exists
        if coins[-1] == -1: return []

        n = len(coins)
        min_cost = [float('inf')] * n  # Initialize min cost array with infinity
        min_cost[-1] = coins[-1]  # The cost of the last coin is the coin value itself

        # Bottom-up dynamic programming approach to compute minimum cost
        for i in range(n - 2, -1, -1):  # Start from the second last element
            if coins[i] != -1:  # If the coin is accessible
                for j in range(i + 1, min(n, i + maxJump + 1)):  # Check for all possible jumps
                    if min_cost[i] > min_cost[j] + coins[i]:  # If a cheaper path is found
                        min_cost[i] = min_cost[j] + coins[i]  # Update min cost for that coin
      
        # If no path exists from the first coin, return empty list
        if min_cost[0] == float('inf'):
            return []
      
        path = []  # To store the cheapest path
        current_cost = min_cost[0]  # Start with min cost of the first coin

        # Reconstruct the path from the min cost array
        for i in range(n):
            if min_cost[i] == current_cost:  # If this coin is part of the cheapest path
                path.append(i + 1)  # Add the coin index (1-based) to the path
                current_cost -= coins[i]  # Subtract the coin's cost from the current cost
      
        # Return the cheapest path
        return path

        def dp(i, path):
            if i == 0:
                return coins[i]
            min_cost = float('inf'), []
            for j in range(1, maxJump + 1):
                if i-j >=0 and coins[i-j] != -1:
                    cur_cost = coins[i] + dp(i - j, path + [i-j])
                    if cur_cost < min_cost:
                        min_cost = cur_cost
                    elif cur_cost == min_cost:
                        if path + coins[i] > min_path:
                            min_path = path + coins[i]
            return min_cost, min_path
            
        cost, path = dp(len(coins) - 1, [])
        return path