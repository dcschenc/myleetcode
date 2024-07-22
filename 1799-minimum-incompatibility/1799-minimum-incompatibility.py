class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subset_size = n // k
        nums.sort()
        
        # Calculate all valid subsets of size subset_size
        valid_subsets = []
        subset_incompatibility = {}
        for subset in itertools.combinations(range(n), subset_size):
            if len(set(nums[i] for i in subset)) == subset_size:
                submask = sum(1 << i for i in subset)
                max_val = max(nums[i] for i in subset)
                min_val = min(nums[i] for i in subset)
                valid_subsets.append(submask)
                subset_incompatibility[submask] = max_val - min_val

        # Initialize DP table
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        # Iterate over all bitmasks
        for mask in range(1 << n):
            if bin(mask).count('1') % subset_size == 0:  # Only consider masks with full subsets
                for submask in valid_subsets:
                    if (mask & submask) == 0:  # If subset is not in the current mask
                        new_mask = mask | submask
                        dp[new_mask] = min(dp[new_mask], dp[mask] + subset_incompatibility[submask])

        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1
