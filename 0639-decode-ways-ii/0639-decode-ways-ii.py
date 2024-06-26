class Solution:
    def numDecodings(self, s: str) -> int:   
        @cache
        def dfs(idx):
            if idx == 0: 
                return 1
            ans = 0
            prev = dfs(idx - 1)
            # Single digit decoding
            if s[idx - 1] == "*":
                ans = 9 * prev
            elif s[idx - 1] != "0":
                ans = prev

            # Two digit decoding
            if idx > 1:
                if s[idx - 2] == "*" and s[idx - 1] == "*":
                    ans += 15 * dfs(idx - 2)
                elif s[idx - 2] == "*":
                    if s[idx - 1] > "6":
                        ans += dfs(idx - 2)
                    else:
                        ans += 2 * dfs(idx - 2)
                elif s[idx - 1] == "*":
                    if s[idx - 2] == "1":
                        ans += 9 * dfs(idx - 2)
                    elif s[idx - 2] == "2":
                        ans += 6 * dfs(idx - 2)
                elif s[idx - 2] != "0" and (ord(s[idx - 2]) - ord("0")) * 10 + ord(s[idx - 1]) - ord("0") <= 26:
                    ans += dfs(idx - 2)

            return ans % mod_val
        
        mod_val = 10**9 + 7
        ans = dfs(len(s))
        return ans % mod_val


        mod_val = 10**9 + 7 
        n = len(s)
        # prev_prev, prev, and current will represent dp[i - 2], dp[i - 1], and dp[i] respectively
        prev_prev, prev, current = 0, 1, 0

        # Iterate over the string
        for i in range(1, n + 1):
            # Single digit decoding
            if s[i - 1] == "*":  
                current = 9 * prev  # '*' can represent any digit from 1 to 9
            elif s[i - 1] != "0":  
                current = prev  # Copy the previous value if the current is not '0'
            else:
                current = 0  # '0' cannot be decoded alone

            # Two digit decoding
            if i > 1:
                # '**' can represent 11 to 19 and 21 to 26, hence 15 possibilities
                if s[i - 2] == "*" and s[i - 1] == "*":
                    current = current + 15 * prev_prev 
                elif s[i - 2] == "*":
                    # If the second digit is 7, 8, or 9, only one combination is possible
                    if s[i - 1] > "6":
                        current = current + prev_prev
                    else:  
                        # If the second digit is 0 to 6, two combinations are possible ('*1' to '*6')
                        current = current + 2 * prev_prev
                elif s[i - 1] == "*":
                    if s[i - 2] == "1":
                        # '1*' can represent 11 to 19, hence 9 possibilities
                        current = current + 9 * prev_prev 
                    elif s[i - 2] == "2":
                        # '2*' can represent 21 to 26, hence 6 possibilities
                        current = current + 6 * prev_prev
                # If both previous and current are not '*' and form a valid number <= 26
                elif (s[i - 2] != "0" and (ord(s[i - 2]) - ord("0")) * 10 + ord(s[i - 1]) - ord("0") <= 26):
                    current = current + prev_prev 

            # Update dp values for the next iteration
            prev_prev, prev = prev, current

        # The current variable now holds the result for the entire string
        return current % mod_val


        @cache
        def backtrack(idx):
            if idx >= n:
                return 1
            ways = 0            
            if s[idx] == '*':
                for i in range(1, 10):
                    ways += backtrack(idx + 1)
            elif 1 <= int(s[idx]) <= 9:
                ways += backtrack(idx + 1)
            # print(idx, s[idx:])
            if idx + 1 < n:
                if s[idx + 1] == '*':
                    for i in range(1, 7):
                        if 10 <= int(s[idx] + str(i)) <= 26:
                            ways += backtrack(idx + 2)
                elif 10 <= int(s[idx:idx + 2]) <= 26:
                    ways += backtrack(idx + 2)  

            return ways
        
        mod = 10 ** 9 + 7
        n = len(s)
        ans = backtrack(0)
        return ans % mod