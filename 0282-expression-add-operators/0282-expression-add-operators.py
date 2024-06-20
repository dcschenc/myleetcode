class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backtrack(idx, cur, path, prev):
            if idx == n:
                if cur == target:
                    res.append(path)
                return   
            for i in range(idx, n):
                if i > idx and num[idx] == '0': break   
                candidate = num[idx: i+1]
                if idx == 0:
                    backtrack(i + 1, int(candidate), candidate, int(candidate))
                else:
                    backtrack(i + 1, cur + int(candidate), path + '+' + candidate, int(candidate))
                    backtrack(i + 1, cur - int(candidate), path + '-' + candidate, -int(candidate))
                    backtrack(i + 1, cur - prev + prev * int(candidate), path + '*' + candidate, prev * int(candidate))
        
        n, res = len(num), []
        backtrack(0, 0, '', -1)
            
        return res


        def backtrack(idx, cur, path, prev):
            if idx == n:
                if cur == target:
                    res.append(path)
                return
            if num[idx] == '0':
                backtrack(idx + 1, cur + 0, path + '+' + num[idx], 0)
                backtrack(idx + 1, cur + 0, path + '-' + num[idx], 0)
                backtrack(idx + 1, cur - prev + prev * 0, path + '*' + num[idx], 0)
                return
            for i in range(idx, n):
                candidate = num[idx: i+1]
                backtrack(i + 1, cur + int(candidate), path + '+' + candidate, int(candidate))
                backtrack(i + 1, cur - int(candidate), path + '-' + candidate, -int(candidate))
                backtrack(i + 1, cur - prev + prev * int(candidate), path + '*' + candidate, prev * int(candidate))
        
        n, res = len(num), []
        for i in range(1, n+1): 
            if i > 1 and num[0] == '0':
                break           
            backtrack(i, int(num[:i]), num[:i], int(num[:i]))
            
        return res