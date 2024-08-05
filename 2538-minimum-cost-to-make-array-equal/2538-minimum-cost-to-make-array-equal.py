class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        costs = cost
        # https://algo.monster/liteproblems/2448
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2448.Minimum%20Cost%20to%20Make%20Array%20Equal
        
        # Combine nums and costs into a list of tuples and sort them by 'nums'
        num_cost_pairs = sorted(zip(nums, costs))
        n = len(num_cost_pairs)
      
        # Prefix sums of costs multiplied by corresponding nums
        prefix_multiplied_costs = [0] * (n + 1)
      
        # Prefix sums of costs
        prefix_costs = [0] * (n + 1)
      
        # Calculate prefix sums
        for i in range(1, n + 1):
            num, cost = num_cost_pairs[i - 1]
            prefix_multiplied_costs[i] = prefix_multiplied_costs[i - 1] + num * cost
            prefix_costs[i] = prefix_costs[i - 1] + cost
      
        # Initialize the answer with infinity representing a very high value
        answer = float('inf')
      
        # Calculate the minimum cost
        for i in range(1, n + 1):
            # Choose the ith element as the 'pivot' number
            pivot = num_cost_pairs[i - 1][0]
          
            # Left part: calculate the total cost for numbers before the 'pivot' number
            left = pivot * prefix_costs[i - 1] - prefix_multiplied_costs[i - 1]
          
            # Right part: calculate the total cost for numbers after the 'pivot' number
            right = prefix_multiplied_costs[n] - prefix_multiplied_costs[i] - pivot * (prefix_costs[n] - prefix_costs[i])
          
            # Update the answer with the minimum sum of left and right parts
            answer = min(answer, left + right)
      
        # Return the minimum cost
        return answer
