class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:    
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1690.Stone%20Game%20VII
        @cache
        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            a = s[j + 1] - s[i + 1] - dfs(i + 1, j)
            b = s[j] - s[i] - dfs(i, j - 1)
            return max(a, b)

        s = list(accumulate(stones, initial=0))
        ans = dfs(0, len(stones) - 1)
        dfs.cache_clear()
        return ans

        @lru_cache(maxsize=None)
        def dp(left, right):
            if left > right: return 0
            choose_left = prefix_sums[right + 1] - prefix_sums[left + 1] - dp(left + 1, right)
            choose_right = prefix_sums[right] - prefix_sums[left] - dp(left, right - 1)

            return max(choose_left, choose_right)

        
        prefix_sums = [0] + list(accumulate(stones))
        dp.cache_clear()
        # Check if the first player's score is non-negative
        ans =  dp(0, len(stones) - 1) 
        dp.cache_clear()
        return ans

        # # Helper function that uses dynamic programming with memoization
        # @lru_cache(maxsize=None)  # Use lru_cache for memoization
        # def dp(low, high):
        #     # Base condition: if no stones are left
        #     if low > high:
        #         return 0
          
        #     # If Alice removes the stone at the low end, the new score is computed
        #     # from the remaining pile (low+1 to high) and current total score
        #     score_when_remove_low = prefix_sums[high + 1] - prefix_sums[low + 1] - dp(low + 1, high)
          
        #     # If Alice removes the stone at the high end, the new score is computed
        #     # from the remaining pile (low to high-1) and current total score
        #     score_when_remove_high = prefix_sums[high] - prefix_sums[low] - dp(low, high - 1)
          
        #     # Return the max score Alice can achieve from the current situation
        #     return max(score_when_remove_low, score_when_remove_high)
      
        # # Construct the prefix sums list where prefix_sums[i] is the sum of stones[0] to stones[i-1]
        # prefix_sums = [0] + list(accumulate(stones))
      
        # # Calculate the maximum score difference Alice can achieve by starting from the full size of the stones pile
        # answer = dp(0, len(stones) - 1)
      
        # # Clear the cache since it is no longer needed
        # dp.cache_clear()
      
        # return answer  # Return the answer


