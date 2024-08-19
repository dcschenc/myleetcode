class Solution:
    def validStrings(self, n: int) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3211.Generate%20Binary%20Strings%20Without%20Adjacent%20Zeros        
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
        
