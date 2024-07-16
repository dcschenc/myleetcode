class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Helper function to perform depth-first search from the current node.
        def dfs(current_node, cost_to_come_back):
            # If the current node has been visited, no need to do anything.
            if visited[current_node]:
                return 0
            visited[current_node] = True
          
            # Accumulated cost of visiting children nodes.
            total_cost = 0
            for child_node in graph[current_node]:
                # Perform DFS on child nodes with the cost of coming back (2 units).
                total_cost += dfs(child_node, 2)
          
            # If there's no apple at the current node, and no cost accumulated from children,
            # it means we don't need to collect any apples on this path.
            if not hasApple[current_node] and total_cost == 0:
                return 0
          
            # Return the total cost of picking apples from this subtree (including the cost to come back).
            return cost_to_come_back + total_cost

        # Construct the graph using adjacency lists.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
      
        # Initialize a visited list to avoid revisiting nodes.
        visited = [False] * n
      
        # Perform a DFS starting at node 0 with no initial cost.
        # Since we start at the root and don't need to return, we pass 0 as the cost.
        return dfs(0, 0)


        def dfs(node, level):
            nonlocal count
            if node not in graph:
                if hasApple[node]:
                    count += 2
                    return True
                return False            
            has_apple = hasApple[node]
            for nb in graph[node]:
                has_apple |= dfs(nb, level + 1)            
            if has_apple:
                count += 2 * level           
            return has_apple
        
        count = 0
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)        
        ans = dfs(0, 0)
        return count
        