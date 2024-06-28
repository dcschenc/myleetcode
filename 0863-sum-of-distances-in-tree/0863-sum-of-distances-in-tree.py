class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # https://algo.monster/liteproblems/834
        # Perform a depth-first search to calculate initial distances and subtree sizes
        def dfs_calculate_dist_and_size(current: int, parent: int, depth: int) -> None:
            total_distance[0] += depth
            subtree_size[current] = 1
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    dfs_calculate_dist_and_size(neighbor, current, depth + 1)
                    subtree_size[current] += subtree_size[neighbor]

        # Perform a second DFS to calculate the answer for each node based on subtree re-rooting
        def dfs_re_root(current: int, parent: int, total_dist: int) -> None:
            # The new total distance is the parent total distance
            # adjusted for moving the root from the parent to the current node
            distances[current] = total_dist
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    new_total_dist = total_dist - subtree_size[neighbor] + (n - subtree_size[neighbor])
                    dfs_re_root(neighbor, current, new_total_dist)

        # Initialize the adjacency list to store the graph
        adjacency_list = defaultdict(list)
        # Store each pair of edges in both directions
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        # Initialize list for distances and sizes
        total_distance = [0]
        subtree_size = [0] * n
        distances = [0] * n

        # First depth-first search: Calculate total distance and subtree sizes
        dfs_calculate_dist_and_size(0, -1, 0)

        # Second depth-first search: Calculate the answer for each node
        dfs_re_root(0, -1, total_distance[0])

        return distances


        # tree = defaultdict(list)
        # count = [1] * N
        # result = [0] * N

        # # Build the tree as an adjacency list
        # for edge in edges:
        #     u, v = edge
        #     tree[u].append(v)
        #     tree[v].append(u)

        # # First BFS pass to calculate the count array
        # queue = deque([0])
        # visited = set([0])

        # while queue:
        #     node = queue.popleft()
        #     for child in tree[node]:
        #         if child not in visited:
        #             visited.add(child)
        #             queue.append(child)
        #             count[child] += count[node]

        # # Second BFS pass to calculate the result array
        # queue = deque([(0, 0)])
        # visited = set([0])

        # while queue:
        #     node, parent_result = queue.popleft()
        #     result[node] = parent_result + (N - count[node])

        #     for child in tree[node]:
        #         if child not in visited:
        #             visited.add(child)
        #             queue.append((child, result[node] - count[child] + N - count[child]))

        # return result

        # # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0834.Sum%20of%20Distances%20in%20Tree

        # def dfs1(node, parent):
        #     for child in tree[node]:
        #         if child != parent:
        #             dfs1(child, node)
        #             count[node] += count[child]
        #             result[node] += result[child] + count[child]

        # def dfs2(node, parent):
        #     for child in tree[node]:
        #         if child != parent:
        #             result[child] = result[node] - count[child] + (n - count[child])
        #             dfs2(child, node)

        # tree = defaultdict(list)
        # count = [1] * n
        # result = [0] * n

        # # Build the tree as an adjacency list
        # for edge in edges:
        #     u, v = edge
        #     tree[u].append(v)
        #     tree[v].append(u)

        # dfs1(0, -1)
        # dfs2(0, -1)

        # return result