class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:  
        def dfs(node):            
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            itinerary.append(node)            

        graph = defaultdict(list)
        # Build the graph
        for start, end in tickets:
            graph[start].append(end)
        # Sort the destinations lexicographically   
        for src in graph:
            graph[src].sort(reverse=True)
        itinerary = []
        dfs("JFK")

        return itinerary[::-1]

       