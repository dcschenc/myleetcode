class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2764.Is%20Array%20a%20Preorder%20of%20Some%20%E2%80%8CBinary%20Tree
        def dfs(node):
            nonlocal idx
            if node != nodes[idx][0]:
                return False
            idx += 1
            for c in tree[node]:
                if dfs(c) is False:
                    return False
            return True           

        tree = defaultdict(list)
        root = -1
        for c, p in nodes:
            if p != -1:
                tree[p].append(c)
            else:
                root = c
        idx = 0
        return dfs(root)