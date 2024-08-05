class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2473.Minimum%20Cost%20to%20Buy%20Apples
        
        # Implementation of Dijkstra's algorithm to find minimum cost from a town
        def dijkstra(start_index):
            # Priority queue to determine which town to visit next, based on the accumulated cost
            priority_queue = [(0, start_index)]          
            # Array to track the minimum distance from the start_index to every other town
            min_distances = [inf] * towns
            min_distances[start_index] = 0
          
            # Initialize answer as infinity
            min_cost = inf
          
            # Loop until there are towns in the priority queue
            while priority_queue:
                # Get the current distance and town index with the lowest cost
                current_distance, current_town = heappop(priority_queue)
              
                # Update the min_cost considering the cost of apples and transportation
                min_cost = min(min_cost, appleCosts[current_town] + current_distance * (multiplier + 1))
              
                # Explore all connected towns
                for adjacent_town, road_cost in graph[current_town]:
                    if min_distances[adjacent_town] > min_distances[current_town] + road_cost:
                        # Update the distance to adjacent_town
                        min_distances[adjacent_town] = min_distances[current_town] + road_cost
                        # Add adjacent_town to priority queue with updated cost
                        heappush(priority_queue, (min_distances[adjacent_town], adjacent_town))
          
            return min_cost
      
        multiplier = k
        towns = n
        appleCosts = appleCost
        
        # Initialize graph as a dictionary of lists to hold all roads between the towns
        graph = defaultdict(list)
      
        # Construct the graph
        for road_start, road_end, road_cost in roads:
            # Adjust indices to be zero-based
            road_start, road_end = road_start - 1, road_end - 1 
            # Add both directions since the roads are bidirectional
            graph[road_start].append((road_end, road_cost))
            graph[road_end].append((road_start, road_cost))
      
        # Compute and return the minimum cost from each town using Dijkstra's algorithm
        return [dijkstra(i) for i in range(towns)]