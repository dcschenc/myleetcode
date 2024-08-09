class Solution:
    def minIncrements(self, n: int, costs: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2673.Make%20Costs%20of%20Paths%20Equal%20in%20a%20Binary%20Tree
        def dfs(node: int) -> int:
            # Base case: If the current node is a leaf node, return its associated cost.
            if (node << 1) > n:
                return costs[node - 1]
          
            # Recursively find the min increment cost of the left and right children.
            left_cost = dfs(node << 1)       # * 2
            right_cost = dfs(node << 1 | 1)  # * 2 + 1
          
            # Update the total increments by adding the difference between the children's costs.
            nonlocal total_increments
            total_increments += abs(left_cost - right_cost)
          
            # Return the cost of this node plus the maximum cost of its children.
            return costs[node - 1] + max(left_cost, right_cost)

        # Initialize the total increments variable.
        total_increments = 0
      
        # Start the depth-first search from the root node (index 1).
        dfs(1)
      
        # Return the total minimum increments to balance the binary tree.
        return total_increments