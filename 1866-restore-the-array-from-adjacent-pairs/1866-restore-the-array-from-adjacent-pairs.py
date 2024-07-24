from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)        
        # Build the graph
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find one endpoint (a node with only one neighbor)
        start = None
        for node in graph:
            if len(graph[node]) == 1:
                start = node
                break
        
        # Reconstruct the array using BFS
        result = []
        queue = deque([start])
        visited = set()
        
        while queue:
            node = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            result.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return result