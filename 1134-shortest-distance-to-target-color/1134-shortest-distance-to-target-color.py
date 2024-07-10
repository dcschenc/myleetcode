class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:    
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1182.Shortest%20Distance%20to%20Target%20Color    
        ## pre compute, left (0, n, use from 1 to n), right (n, 0, use from n-1 to 0) ####
        n = len(colors)
        left = [[-inf] * 3 for _ in range(n + 1)]       
        for i in range(1, n + 1):
            color = colors[i-1] - 1
            for j in range(3):
                left[i][j] = left[i - 1][j]
            left[i][color] = i - 1

        right = [[inf] * 3 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(3):
                right[i][j] = right[i + 1][j]
            right[i][color] = i

        ans = []
        for i, color in queries:
            d = min(i - left[i + 1][color - 1], right[i][color - 1] - i)
            ans.append(-1 if d > n else d)
        return ans

        
        # n = len(colors)
        # left = [{}] * n
        # prev = {1:float('inf'), 2: float('inf'), 3: float('inf')}
        # for i in range(n):
        #     prev[colors[i]] = i
        #     left[i] = prev.copy()
        # right = [{}] * n
        # prev = {1:float('inf'), 2: float('inf'), 3: float('inf')}
        # for i in range(n-1, -1, -1):
        #     prev[colors[i]] = i
        #     right[i] = prev.copy()
        # ans = []
        # for idx, color in queries:
        #     min_idx = min(abs(idx - left[idx][color]), abs(idx - right[idx][color]))
        #     if min_idx == float('inf'):
        #         min_idx = -1
        #     ans.append(min_idx)
        # return ans