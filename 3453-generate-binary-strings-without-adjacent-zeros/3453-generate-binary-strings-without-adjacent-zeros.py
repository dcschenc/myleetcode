class Solution:
    def validStrings(self, n: int) -> List[str]:
        def backtrack(i, path):
            if i == n:
                ans.append(path)
                return
            if path[-1] == '0':
                backtrack(i + 1, path + '1')
            if path[-1] == '1':
                backtrack(i + 1, path + '0')
                backtrack(i + 1, path + '1')
        
        ans = []
        backtrack(1, '0')
        backtrack(1, '1')
        return ans
        
