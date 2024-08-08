class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2638.Count%20the%20Number%20of%20K-Free%20Subsets

        # Sort the numbers in ascending order
        nums.sort()
      
        # Group numbers by their remainder when divided by k
        remainder_groups = defaultdict(list)
        for num in nums:
            remainder_groups[num % k].append(num)
      
        # Initialize answer as 1
        ans = 1      
        # Loop through each group of numbers with the same remainder
        for group in remainder_groups.values():
            group_size = len(group)
            # The dp array holds the count of k-free subsets up to the current index
            dp = [0] * (group_size + 1)
            dp[0] = 1  # One way to create a subset including no elements
            dp[1] = 2  # Two ways to create a subset including the first element
          
            # Calculate the number of k-free subsets for the current group
            for i in range(2, group_size + 1):
                # If the difference between current and previous is k, we may merge the last two sets
                if group[i - 1] - group[i - 2] == k:
                    dp[i] = dp[i - 1] + dp[i - 2]
                else:
                    # Otherwise, we can either include or exclude the current number
                    dp[i] = dp[i - 1] * 2
          
            # Multiply the result by the number of k-free subsets for the current group
            ans *= dp[group_size]
      
        # Return the total number of k-free subsets
        return ans

        nums.sort()
        g = defaultdict(list)
        for x in nums:
            g[x % k].append(x)
        ans = 1
        for arr in g.values():
            m = len(arr)
            f = [0] * (m + 1)
            f[0] = 1
            f[1] = 2
            for i in range(2, m + 1):
                if arr[i - 1] - arr[i - 2] == k:
                    f[i] = f[i - 1] + f[i - 2]
                else:
                    f[i] = f[i - 1] * 2
            ans *= f[m]
        return ans

