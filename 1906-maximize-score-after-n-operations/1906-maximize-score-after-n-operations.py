class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def backtrack(idx):
            # If we've performed N operations, return 0
            if idx == n // 2:
                return 0
            
            # Use a tuple of used indices as a key for memoization
            key = tuple(used)
            if key in memo:
                return memo[key]
            
            max_result = 0
            
            # Iterate through all pairs
            for i in range(n):
                if used[i]: continue
                for j in range(i + 1, n):
                    if used[j]: continue
                    
                    # Mark these indices as used
                    used[i] = used[j] = True
                    
                    # Calculate score for this operation
                    current_score = math.gcd(nums[i], nums[j]) * (idx + 1)
                    
                    # Recur for the next operation
                    max_result = max(max_result, current_score + backtrack(idx + 1))
                    
                    # Backtrack (unmark the indices)
                    used[i] = used[j] = False
            
            memo[key] = max_result
            return max_result

        n = len(nums)  # Number of operations
        max_score = 0
        memo = {}
        # Start the backtracking with all indices unused and operation index 0
        used = [False] * len(nums)
        max_score = backtrack(0)
        
        return max_score