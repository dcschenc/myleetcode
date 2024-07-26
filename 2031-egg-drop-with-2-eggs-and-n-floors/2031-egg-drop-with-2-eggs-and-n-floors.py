class Solution:
    def twoEggDrop(self, n: int) -> int:
        # Test highest limit of given eggs with minimal movement
        @cache
        def dfs(eggs, floors): 
            # Last one egg remains, only one way to test from 1F, 2F, ... to N-th Floor
            if eggs == 1: return floors

            # No more floors, no need to test anymore
            if floors == 0: return 0 

            # Compute minimal movement to cover all worst cases of testing results
            min_move = math.inf 
            for f in range(1, floors + 1): 
                is_borken = dfs(eggs - 1, f - 1)
                is_safe = dfs(eggs, floors - f)

                # Minimize movement between worst case of {egg broken, or egg safe}
                # current cost 1 + worst case of {egg broken, or egg safe}
                min_move = min(min_move, 1 + max(is_borken, is_safe) )

            # Update DP table with minimal move to test floors with given specific eggs
            # dp[floors, eggs] = min_move
            return min_move 
        # =======================
        return dfs(2, n)
        
        # Initialize a DP table with (2 + 1) x (n + 1)
        dp = [[0] * (n + 1) for _ in range(3)]
        
        # Fill the DP table
        for j in range(1, n + 1):
            dp[1][j] = j  # With one egg, we need j attempts for j floors
        
        for i in range(2, 3):  # For 2 eggs
            for j in range(1, n + 1):
                dp[i][j] = float('inf')
                low, high = 1, j
                while low <= high:
                    mid = (low + high) // 2
                    break_count = dp[i-1][mid-1]
                    not_break_count = dp[i][j-mid]
                    worst_case = 1 + max(break_count, not_break_count)
                    
                    dp[i][j] = min(dp[i][j], worst_case)
                    
                    if break_count > not_break_count:
                        high = mid - 1
                    else:
                        low = mid + 1
        
        return dp[2][n]

    # https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/solutions/4720115/python-by-top-down-dp-w-comment/
        # DP Table
        # key: (floors, eggs)
        # value: corresponding minimal movement
        # dp = {}

        # Test highest limit of given eggs with minimal movement
        @cache
        def test(floors, eggs): 
            # if (floors, eggs) in dp:
                # return dp[floors, eggs]

            # Last one egg remains, only one way to test from 1F, 2F, ... to N-th Floor
            ## 只有一个蛋了，只能从下往上
            if eggs == 1: return floors

            # No more floors, no need to test anymore
            if floors == 0: return 0 

            # Compute minimal movement to cover all worst cases of testing results
            min_move = math.inf 
            for f in range(1, floors+1): 
                is_borken = test(f-1, eggs-1)
                is_safe = test(floors-f, eggs)

                # Minimize movement between worst case of {egg broken, or egg safe}
                #                        current cost 1 + worst case of {egg broken, or egg safe}
                min_move = min(min_move, 1 + max(is_borken, is_safe) )

            # Update DP table with minimal move to test floors with given specific eggs
            # dp[floors, eggs] = min_move
            return min_move 
        # =======================
        return test(floors=n, eggs=2)

    # https://algo.monster/liteproblems/1884    
        def drop(k: int, n: int) -> int:
            if k == 0:
                return 0
            if k == 1:
                return n
            if n == 0:
                return 0
            if n == 1:
                return 1
            if dp[k][n] != -1:
                return dp[k][n]
            
            l, r = 1, n + 1

            while l < r:
                m = (l + r) // 2
                broken = drop(k - 1, m - 1)
                unbroken = drop(k, n - m)
                if broken >= unbroken:
                    r = m
                else:
                    l = m + 1

            dp[k][n] = 1 + drop(k - 1, l - 1)
            return dp[k][n]

        dp = [[-1] * (n + 1) for _ in range(3)]
        return drop(2, n)
