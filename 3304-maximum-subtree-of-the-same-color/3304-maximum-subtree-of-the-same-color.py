class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3004.Maximum%20Subtree%20of%20the%20Same%20Color
        def dfs(node):
            if node not in tree:
                return True, 1
            color = colors[node]
            same, total = True, 0
            for c in tree[node]:
                same_child, total_child = dfs(c)
                if colors[c] != color or same_child == False:
                    same = False                
                total += total_child
            if same:
                ans[0] = max(ans[0], 1 + total)
            return same, 1 + total

        n = len(colors)
        tree = defaultdict(list)
        for p, c in edges:
            tree[p].append(c)
        ans = [1]
        dfs(0)
        return ans[0]