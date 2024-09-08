class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0815.Bus%20Routes
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0815.Bus%20Routes

        if source == target:
            return 0
        # Convert each route to a set for faster checks later on.
        sets_of_routes = [set(route) for route in routes]      
        # Create a dictionary where each stop maps to a list of buses (routes) that visit that stop.
        stop_dict = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_dict[stop].append(i)
      
        # Build a graph where each node represents a bus and edges connect buses that share a common stop.
        graph = defaultdict(list)
        for buses in stop_dict.values():
            num_buses = len(buses)
            for i in range(num_buses):
                for j in range(i + 1, num_buses):
                    first, second = buses[i], buses[j]
                    graph[first].append(second)
                    graph[second].append(first)
      
        # Start BFS from the buses that can be taken from the source stop.
        queue = deque(stop_dict[source])
        ans = 1
        visited = set()      
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()              
                # If the target stop is in the current bus's route, return the number of buses needed.
                if target in sets_of_routes[cur]:
                    return ans
                if cur in visited:
                    continue
                visited.add(cur)              
                # Check unvisited buses that can be reached from the current bus.
                for adjacent_bus in graph[cur]:
                    if adjacent_bus not in visited:
                        queue.append(adjacent_bus)          
            ans += 1
      
        return -1
