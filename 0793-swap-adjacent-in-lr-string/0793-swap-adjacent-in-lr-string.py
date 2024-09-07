class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0777.Swap%20Adjacent%20in%20LR%20String
        # First, check if the non-'X' characters match
        if start.replace('X', '') != end.replace('X', ''):
            return False
        
        # Now, check the valid moves for 'L' and 'R'
        i, j = 0, 0
        n = len(start)
        
        while i < n and j < n:
            # Skip all 'X' in both strings
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            
            # If one string is exhausted while the other isn't, it's not possible
            if (i < n) != (j < n):
                return False
            
            # If both pointers are valid, check the positions
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                # For 'L', i must be >= j since 'L' can only move left
                if start[i] == 'L' and i < j:
                    return False
                # For 'R', i must be <= j since 'R' can only move right
                if start[i] == 'R' and i > j:
                    return False
                i += 1
                j += 1
        
        return True

    