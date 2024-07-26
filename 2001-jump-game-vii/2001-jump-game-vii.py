class Solution:
    def canReach(self, s: str, min_jump: int, max_jump: int) -> bool:    
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1871.Jump%20Game%20VII
        n = len(s)
        pre = [0] * (n + 1)
        pre[1] = 1
        f = [True] + [False] * (n - 1)
        for i in range(1, n):
            if s[i] == "0":
                l, r = max(0, i - max_jump), i - min_jump
                f[i] = l <= r and pre[r + 1] - pre[l] > 0
            pre[i + 1] = pre[i] + f[i]
        return f[-1]

        arr = s
        # Length of the input string
        length = len(arr)
      
        # A dynamic programming list to keep track of the possibility to reach each index
        can_reach = [False] * length
      
        # The starting point is always reachable
        can_reach[0] = True
      
        # Prefix sum array to keep track of number of reachable points in the string up to index i
        prefix_sum = [0] * (length + 1)

        # Initially only the first point is reachable
        prefix_sum[1] = 1
      
        # Loop through each point in the string
        for i in range(1, length):
            # We only need to consider '0' positions since '1' positions are not reachable
            if arr[i] == '0':
                # Calculate the range of jumps
                left_bound = max(0, i - max_jump) # Lower bound for the jump
                right_bound = i - min_jump        # Upper bound for the jump
              
                # If the sum of reachable points between the bounds is greater than 0, 
                # then the current point is reachable
                if right_bound >= left_bound and prefix_sum[right_bound + 1] - prefix_sum[left_bound] > 0:
                    can_reach[i] = True
          
            # Update the prefix sum array with the reachability of the current index
            prefix_sum[i + 1] = prefix_sum[i] + int(can_reach[i])
      
        # Check if the last point is reachable, return the result
        return can_reach[length - 1]
            
        n = len(s)
        if s[n-1] == '1': 
            return False
        a, b = minJump, maxJump
        j = b
        if a <= n - 1 and b >= n - 1: 
            return True
        while j >= a and j <= n - 1:            
            if s[j] == '0':
                a, b = j + minJump, j + maxJump
                j = b
                if a <= n - 1 and b >= n - 1: 
                    return True
            else:
                j -= 1
        return False
