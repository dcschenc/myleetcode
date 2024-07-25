class Solution:
    def splitString(self, s: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1849.Splitting%20a%20String%20Into%20Descending%20Consecutive%20Values
        def dfs(i, x, k):
            if i == len(s):
                return k > 1
            y = 0
            for j in range(i, len(s)):
                y = y * 10 + int(s[j])
                if (x == -1 or x - y == 1) and dfs(j + 1, y, k + 1):
                    return True
            return False

        return dfs(0, -1, 0)
        
        def backtrack(target, idx):
            if idx == len(s):
                return True
            for i in range(idx + 1, len(s) + 1):
                if int(s[idx:i]) == target:
                    if backtrack(target - 1, i):
                        return True                   
            return False
        
        for i in range(1, len(s)):
            target = int(s[:i])            
            if backtrack(target - 1, i):
                return True            
        return False
            