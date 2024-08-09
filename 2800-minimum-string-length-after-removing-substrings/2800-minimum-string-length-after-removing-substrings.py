class Solution:
    def minLength(self, s: str) -> int:        
        stk = [""]
        for c in s:
            if (c == "B" and stk[-1] == "A") or (c == "D" and stk[-1] == "C"):
                stk.pop()
            else:
                stk.append(c)
        return len(stk) - 1
        
        # while True:
        #     i, n = 0, len(s)
        #     new = ''
        #     while i < n-1:
        #         if s[i:i+2] in ['AB', 'CD']:                              
        #             i += 2
        #         else:
        #             new += s[i]
        #             i += 1
        #     if i == n-1:
        #         new += s[i]
        #     if len(new) == len(s):
        #         break
        #     s = new
        # return len(s)
        