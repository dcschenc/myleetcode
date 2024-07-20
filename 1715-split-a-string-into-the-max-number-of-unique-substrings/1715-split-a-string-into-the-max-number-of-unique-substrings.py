class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1593.Split%20a%20String%20Into%20the%20Max%20Number%20of%20Unique%20Substrings
        def backtrack(idx, path):
            nonlocal ans
            if idx == n:                
                if len(path) > len(ans):
                    ans = path 
                return
            for i in range(idx, n):
                candidate = s[idx: i+1]
                if candidate not in path:
                    backtrack(i+1, path + [candidate])
        
        ans, n = [], len(s)
        backtrack(0, [])
        return len(ans)