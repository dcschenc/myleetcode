class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2184.Number%20of%20Ways%20to%20Build%20Sturdy%20Brick%20Wall
        def dfs(v):   # to build possible lays
            if v > width:
                return
            if v == width:
                s.append(t[:])
                return
            for x in bricks:
                t.append(x)
                dfs(v + x)
                t.pop()

        def check(a, b):  # to check 2 lays can be one on top of the other
            s1, s2 = a[0], b[0]
            i = j = 1
            while i < len(a) and j < len(b):
                if s1 == s2:
                    return False
                if s1 < s2:
                    s1 += a[i]
                    i += 1
                else:
                    s2 += b[j]
                    j += 1
            return True

        mod = 10**9 + 7
        s = []
        t = []
        dfs(0)
        g = defaultdict(list)
        n = len(s)
        for i in range(n):
            if check(s[i], s[i]):
                g[i].append(i)
            for j in range(i + 1, n):
                if check(s[i], s[j]):
                    g[i].append(j)
                    g[j].append(i)
        dp = [[0] * n for _ in range(height)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, height):
            for j in range(n):
                for k in g[j]:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod
        return sum(dp[-1]) % mod


        # https://algo.monster/liteproblems/2184
        # Helper function to find all possible ways to build a single layer
        def build_layer(current_width):  ## dfs
            if current_width > width:
                return
            if current_width == width:
                all_layers.append(layer[:])
                return
            for brick in bricks:
                layer.append(brick)
                build_layer(current_width + brick)
                layer.pop()

        # Function to check if two configurations can be placed one over the other
        def is_compatible(layer1, layer2):
            sum1, sum2 = layer1[0], layer2[0]
            index1, index2 = 1, 1
            while index1 < len(layer1) and index2 < len(layer2):
                if sum1 == sum2:
                    return False
                if sum1 < sum2:
                    sum1 += layer1[index1]
                    index1 += 1
                else:
                    sum2 += layer2[index2]
                    index2 += 1
            return True

        mod = 10**9 + 7
        all_layers = []  # To store all possible configurations for one layer
        layer = []  # To store the current layer configuration
        build_layer(0)  # Build layers starting with 0 width

        adjacency_list = defaultdict(list)  # To store the graph of compatible layers
        num_layers = len(all_layers)

        # Build the graph
        for i in range(num_layers):
            if is_compatible(all_layers[i], all_layers[i]):
                adjacency_list[i].append(i)
            for j in range(i + 1, num_layers):
                if is_compatible(all_layers[i], all_layers[j]):
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        # Dynamic programming array initialization
        dp = [[0] * num_layers for _ in range(height)]
        for j in range(num_layers):
            dp[0][j] = 1  # Each configuration is one way to build the first layer

        # Compute number of ways to build the wall using DP
        for i in range(1, height):
            for j in range(num_layers):
                for k in adjacency_list[j]:
                    dp[i][j] += dp[i - 1][k]
                    dp[i][j] %= mod

        return sum(dp[-1]) % mod  # Return the number of ways modulo 10^9 + 7