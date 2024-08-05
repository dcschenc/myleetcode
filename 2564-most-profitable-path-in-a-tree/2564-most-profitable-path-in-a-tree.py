class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2467.Most%20Profitable%20Path%20in%20a%20Tree
        
        # Initialize Depth-First Search to determine the number of steps to reach Node 0 from start
        def dfs_time_to_reach(i, prev, t):
            # If we've reached Node 0, update the time and return True
            if i == 0:
                time_to_reach[i] = min(time_to_reach[i], t)
                return True
            # Traverse the graph
            for neighbor in graph[i]:
                if neighbor != prev and dfs_time_to_reach(neighbor, i, t + 1):
                    # Update the time for each node as we find a shorter path
                    time_to_reach[neighbor] = min(time_to_reach[neighbor], t + 1)
                    return True
            return False

        # Perform DFS to calculate the most profitable value while traveling towards Node 0
        def dfs_max_profit(i, prev, t, current_profit):
            # Collect the profit according to the rules described
            if t == time_to_reach[i]:
                current_profit += amount[i] // 2
            elif t < time_to_reach[i]:
                current_profit += amount[i]
            nonlocal max_profit
            # If it's a leaf node, update the max_profit if the current_profit is higher
            if len(graph[i]) == 1 and graph[i][0] == prev:
                max_profit = max(max_profit, current_profit)
                return
            # Continue DFS on the graph
            for neighbor in graph[i]:
                if neighbor != prev:
                    dfs_max_profit(neighbor, i, t + 1, current_profit)

        num_nodes = len(edges) + 1
        graph = defaultdict(list)
        time_to_reach = [num_nodes] * num_nodes  # Initialize with a large number
        # Convert edge list to a graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        # Start DFS to determine time to reach Node 0 for bob
        dfs_time_to_reach(bob, -1, 0)
        time_to_reach[bob] = 0  # Set the start node time to 0
        max_profit = float('-inf')  # Initialize maximum profit as negative infinity
        # Start DFS to determine max profit
        dfs_max_profit(0, -1, 0, 0)
        return max_profit
