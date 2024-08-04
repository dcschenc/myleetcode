class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2378.Choose%20Edges%20to%20Maximize%20Score%20in%20a%20Tree
        # def dfs(i):
        #     a = b = t = 0
        #     for j, w in g[i]:
        #         x, y = dfs(j)
        #         a += y
        #         b += y
        #         t = max(t, x - y + w)
        #     b += t
        #     return a, b

        # g = defaultdict(list)
        # for i, (p, w) in enumerate(edges[1:], 1):
        #     g[p].append((i, w))
        # return dfs(0)[1]

        # Depth-First Search (DFS) function to traverse graph and calculate score
        def dfs(node_index):
            base_score = best_score = total_gain = 0
            # Exploring all children nodes and their respective weights
            for child_index, weight in graph[node_index]:
                child_base, child_best = dfs(child_index)
                base_score += child_best
                best_score += child_best
                total_gain = max(total_gain, child_base - child_best + weight)
            # Updating best score to account for the total gain from the most profitable child
            best_score += total_gain
            return base_score, best_score

        # Convert edge list to graph representation for easier traversal
        graph = defaultdict(list)
        for index, (parent, weight) in enumerate(edges[1:], 1):
            graph[parent].append((index, weight))
      
        # Initiate DFS from the root node (index 0) and return the best score
        return dfs(0)[1]