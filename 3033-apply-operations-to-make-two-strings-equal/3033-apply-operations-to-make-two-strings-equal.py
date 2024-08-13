class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        @lru_cache(maxsize=None)  # Cache results to avoid recomputation
        def dfs(i: int, j: int) -> int:
            # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2896.Apply%20Operations%20to%20Make%20Two%20Strings%20Equal
            # Base case: If the pointers cross each other, return 0 since we don't need to make operations.
            if i > j: return 0
          
            # Recurrence relation:
            # 1. Swap any character in s1 with 'x' and solve for the smaller substring.
            swap_with_x = dfs(i + 1, j - 1) + x

            # 2. Move the first pointer by two and add the difference between current and previous indices.
            # This essentially skips one element that doesn't need changes.
            skip_left = dfs(i + 2, j) + idx[i + 1] - idx[i]

            # 3. Move the second pointer by two and add the difference between current and previous indices.
            # This skips one element from the end that doesn't need changes.
            skip_right = dfs(i, j - 2) + idx[j] - idx[j - 1]

            # Return the minimum operations among the three alternatives.
            return min(swap_with_x, skip_left, skip_right)

        # Step 1: Identify indices where the characters in s1 and s2 differ.
        idx = [i for i in range(len(s1)) if s1[i] != s2[i]]
        # Number of indices that are different in s1 and s2.
        n = len(idx)
        # Step 2: If there is an odd number of different indices, it's impossible to make s1 equal to s2, return -1.
        if n % 2: return -1      
        # Step 3: Apply the dfs function to the entire range of different indices.
        return dfs(0, n - 1)