class Solution:
    def minimizeResult(self, expression: str) -> str:
        l, r = expression.split("+")
        m, n = len(l), len(r)
        mi = inf
        ans = None
        for i in range(m):
            for j in range(n):
                c = int(l[i:]) + int(r[: j + 1])
                a = 1 if i == 0 else int(l[:i])
                b = 1 if j == n - 1 else int(r[j + 1 :])
                if (t := a * b * c) < mi:
                    mi = t
                    ans = f"{l[:i]}({l[i:]}+{r[: j + 1]}){r[j + 1:]}"
        return ans
        
        # s = expression
        # n = len(s)
        # plus = s.index('+')
        # ans = float('inf')
        # left, right = 0, 0
        # for i in range(plus):
        #     a = int(s[:i]) if i > 0 else 1           
        #     b = int(s[i:plus])        
        #     for k in range(plus+1, n):
        #         c = int(s[plus+1:k+1])
        #         if k == n-1:
        #             d = 1
        #             if a * (b + c) * d < ans:
        #                 ans = a * (b + c) * d
        #                 left, right = i, n
        #                 print(ans, a,b,c,d)
        #         else:
        #             for l in range(k, n-1):
        #                 d = int(s[l:]) 
        #                 if a * (b + c) * d < ans:
        #                     ans = a * (b + c) * d
        #                     left, right = i, l
        #                     print(ans, a,b,c,d)
        # s = s[:left] + '(' + s[left:right] + ')' + s[right:]
        # return s
