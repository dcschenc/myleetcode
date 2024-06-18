class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            i = 0
            t = []
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                t.append(str(j - i))
                t.append(str(s[i]))
                i = j
            s = ''.join(t)
        return s
        
        pre = '1'
        for i in range(2, n + 1):
            cur = ''
            count = 0
            for j in range(len(pre)):
                if j == 0 or pre[j] == pre[j-1]:
                    count += 1                    
                else:
                    cur += str(count) + pre[j-1]
                    count = 1
            cur += str(count) + pre[-1]
            pre = cur
        return pre
