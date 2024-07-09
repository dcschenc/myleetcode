# Build a weighted graph where each house is a node, and each pipe or well is an edge with its corresponding cost.
# Run Prim's Algorithm:

# Start from any arbitrary node (for example, the central well) and iteratively add the minimum-cost edge that connects a node in the growing minimum spanning tree to a node outside the tree.
# Calculate the Minimum Cost:

# The sum of the weights of the edges in the minimum spanning tree will be the minimum cost to supply water to all houses

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Build the weighted graph
        graph = defaultdict(list)
        for i, well_cost in enumerate(wells):
            graph[0].append((i + 1, well_cost))  # Central well to houses

        for house1, house2, pipe_cost in pipes:
            graph[house1].append((house2, pipe_cost))
            graph[house2].append((house1, pipe_cost))

        # Run Prim's Algorithm
        min_cost = 0
        visited = set()
        min_heap = [(0, 0)]  # (cost, node)

        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            min_cost += cost
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_cost, neighbor))

        return min_cost