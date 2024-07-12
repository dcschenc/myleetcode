class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1273.Delete%20Tree%20Nodes
        def dfs(node):
            total = value[node]
            subtree = set()
            subtree.add(node)
            for ch in tree[node]:
                total_child, subtree_child = dfs(ch)
                total += total_child
                subtree.update(subtree_child)
            if total == 0:
                to_delete.update(subtree)
            return total, subtree

        tree, to_delete = defaultdict(list), set()
        for i in range(nodes):
            if parent[i] != -1:
                tree[parent[i]].append(i)
        dfs(0)
        return nodes - len(to_delete)