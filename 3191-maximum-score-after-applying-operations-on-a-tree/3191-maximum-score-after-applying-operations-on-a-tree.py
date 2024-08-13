class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2925.Maximum%20Score%20After%20Applying%20Operations%20on%20a%20Tree
        def dfs(node, parent):
            total = values[node]           
            child_dp, child_sum = 0, 0
            for child in tree[node]:
                if child != parent:
                    total += dfs(child, node)
                    child_dp += dp[child]
                    child_sum += s[child]
            s[node] = total
            if child_sum == 0:
                dp[node] = 0
            else:
                dp[node] = max(values[node] + child_dp, child_sum)
            return s[node]

        n = len(values)
        ### dp: the max score each node can acheive, s: the total sum of each node ####
        dp, s = [0] * n, [0] * n
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)        
        dfs(0, -1)
        return dp[0]