class Solution:
    def confusingNumberII(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1088.Confusing%20Number%20II
        def check(x: int) -> bool:
            y, t = 0, x
            while t:
                t, v = divmod(t, 10)
                y = y * 10 + d[v]
            return x != y

        def dfs(pos: int, limit: bool, x: int) -> int:
            if pos >= len(s):
                return int(check(x))
            up = int(s[pos]) if limit else 9
            ans = 0
            for i in range(up + 1):
                if d[i] != -1:
                    ans += dfs(pos + 1, limit and i == up, x * 10 + i)
            return ans

        d = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        s = str(n)
        return dfs(0, True, 0)


        def is_confusing(n_str: int) -> bool:
            # special case - single digit
            if len(n_str)==1:
                return n_str not in {'0', '1', '8'}            
            left = 0
            right = len(n_str)-1
            while left<=right:
                if matching[n_str[left]]!=n_str[right]:
                    return True
                left+=1
                right-=1
            return False

        def backtrack(val_str, val):
            nonlocal total
            if 1 <= val <= n:
                if is_confusing(val_str):
                    total += 1
            elif val > n:
                return

            for c in matching.keys():
                if val==0:
                    if c=='0':
                        continue
                    backtrack(val_str + c, val*10 + int(c))
                # has at least 1 digit
                else: 
                    backtrack(val_str + c, val*10 + int(c))

        matching = {'1':'1', '6':'9', '9':'6', '8':'8', '0':'0'}
        total = 0
        backtrack('', 0)
        return total
