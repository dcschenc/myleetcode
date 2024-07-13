class Solution:
    def freqAlphabets(self, s: str) -> str:
        def get(s):
            return chr(ord('a') + int(s) - 1)

        i, n = 0, len(s)
        res = []
        while i < n:
            if i + 2 < n and s[i + 2] == '#':
                res.append(get(s[i : i + 2]))
                i += 3
            else:
                res.append(get(s[i]))
                i += 1
        return ''.join(res)
        
        hm = {}
        for i in range(10, 27):
            hm[str(i) + '#'] = chr(ord('a') + i - 1)
        # print(hm)
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                c = hm[stack[-2] + stack[-1] + '#']
                stack.pop()
                stack.pop()
                stack.append(c)
            else:
                stack.append(s[i])
            i += 1
        ans = ''
        for c in stack:
            if c.isdigit(): 
                ans += chr(ord('a') + int(c) - 1)
            else:
                ans += c
        return ans
        
