class Solution:
    def minFlips(self, target: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1529.Minimum%20Suffix%20Flips
        if not target:
            return 0

        flips = 0
        current_state = '0'
        
        for char in target:
            if char != current_state:
                flips += 1
                current_state = char
        
        return flips