class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1931.Painting%20a%20Grid%20With%20Three%20Different%20Colors
        # https://algo.monster/liteproblems/1931
        def is_valid_pattern(pattern: int) -> bool:
            last_color = -1
            for _ in range(m):
                current_color = pattern % 3
                if current_color == last_color:
                    return False
                last_color = current_color
                pattern //= 3
            return True

        # Helper function to check if two adjacent columns' coloring patterns are valid
        def are_adjacent_patterns_valid(first: int, second: int) -> bool:
            for _ in range(m):
                if first % 3 == second % 3:
                    return False
                first, second = first // 3, second // 3
            return True

        # Mod value for the final result to prevent integer overflow
        mod = 10**9 + 7
      
        # The maximum value for a coloring pattern
        max_pattern_value = 3**m
      
        # Set of all valid coloring patterns
        valid_patterns = {i for i in range(max_pattern_value) if is_valid_pattern(i)}
      
        # Dictionary that maps each valid pattern to other patterns which it can be adjacent to
        adjacent_patterns = defaultdict(list)
        for pattern in valid_patterns:
            for adjacent in valid_patterns:
                if are_adjacent_patterns_valid(pattern, adjacent):
                    adjacent_patterns[pattern].append(adjacent)
      
        # List storing the number of ways to color each pattern for a single column
        ways_to_color = [int(pattern in valid_patterns) for pattern in range(max_pattern_value)]
      
        # Iterate over all columns from the second to the last to calculate possible colorings
        for _ in range(n - 1):
            next_column_ways = [0] * max_pattern_value
            # Iterate over each valid pattern
            for pattern in valid_patterns:
                # Add up the ways to color this pattern based on its adjacent patterns from previous column
                for adjacent in adjacent_patterns[pattern]:
                    next_column_ways[pattern] = (next_column_ways[pattern] + ways_to_color[adjacent]) % mod
            ways_to_color = next_column_ways
      
        # Sum all the ways to color the final column
        return sum(ways_to_color) % mod


        @functools.lru_cache(None)
        def generate(i):
            if i == m:
                return [""]
            ans = []
            for s in {"r", "b", "g"}:
                for j in generate(i+1):
                    if not j or s != j[0]:
                        ans.append(s+j)
            return ans
            
        @functools.lru_cache(None)
        def dp(i, prev):
            if i == n:
                return 1
            ans = 0
            if not prev:
                for p in generate(0):
                    ans += dp(i + 1, p)
            else:
                for p in generate(0):
                    for k in range(len(p)):
                        if p[k] == prev[k]:
                            break
                    else:
                        ans += dp(i+1, p)
            return ans 
  
        return dp(0, "") % (10**9 + 7)