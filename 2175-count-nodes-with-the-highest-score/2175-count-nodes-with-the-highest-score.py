class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2049.Count%20Nodes%20With%20the%20Highest%20Score
        def dfs(node):
            left, right, score = 0, 0, 1
            if node in tree:
                left = dfs(tree[node][0])
                score *= left
                if len(tree[node]) == 2:
                    right = dfs(tree[node][1])
                    score *= right
            rest = n - left - right - 1
            if rest:
                score *= rest
            hm[score].append(node)            
            return left + right + 1

        hm = defaultdict(list)
        tree = defaultdict(list)
        n = len(parents)
        for i in range(n):
            if parents[i] != -1:
                tree[parents[i]].append(i)
        dfs(0)
        mx = max(hm.keys())
        return len(hm[mx])