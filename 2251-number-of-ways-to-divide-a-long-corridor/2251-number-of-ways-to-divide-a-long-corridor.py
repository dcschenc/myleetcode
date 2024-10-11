class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2147.Number%20of%20Ways%20to%20Divide%20a%20Long%20Corridor
        MOD = 10**9 + 7
        n = len(corridor)
        seat_count = corridor.count('S')
        
        # If there aren't exactly 2n seats, it's impossible to partition as required
        if seat_count < 2 or seat_count % 2 != 0:
            return 0

        # List to store the indices of all seats in the corridor
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        # DFS function with memoization
        memo = {}
        def dfs(index):
            # If we've reached the last pair of seats, there's only one way to end
            if index == len(seats) - 1:
                return 1
            
            if index in memo:
                return memo[index]
            
            # Find the gap between this seat and the next
            gap = seats[index + 1] - seats[index]
            
            # Calculate the number of ways recursively
            memo[index] = (gap * dfs(index + 2)) % MOD
            return memo[index]
        
        # Start DFS from the first seat pair
        return dfs(1)