class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        # Initial mismatch counts
        xy_count = 0
        yx_count = 0
        
        # Count the mismatches
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy_count += 1
            elif a == 'y' and b == 'x':
                yx_count += 1
        
        # If the sum of mismatches is odd, it's impossible to fix
        if (xy_count + yx_count) % 2 != 0:
            return -1
        
        # Number of swaps needed
        # Each pair of 'xy' and 'yx' can be fixed with one swap
        # If there are odd number of 'xy' or 'yx', we need two additional swaps to fix the last unmatched pair
        return (xy_count // 2) + (yx_count // 2) + (2 if xy_count % 2 != 0 else 0)