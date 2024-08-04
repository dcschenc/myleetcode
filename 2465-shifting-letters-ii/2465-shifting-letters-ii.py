class Solution:
    # https://algo.monster/liteproblems/2381
    # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2381.Shifting%20Letters%20II
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:        
            if direction == 0:                
                direction = -1
            diff[start] += direction
            diff[end + 1] -= direction
        for i in range(1, n + 1):
            diff[i] += diff[i-1]

        for i in range(n):
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + diff[i] + 26)%26)
        return ''.join(s)
        