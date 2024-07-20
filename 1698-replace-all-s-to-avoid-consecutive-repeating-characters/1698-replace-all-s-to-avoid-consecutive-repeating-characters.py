class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            if s[i] == "?":
                for c in "abc":
                    if (i and s[i - 1] == c) or (i + 1 < n and s[i + 1] == c):
                        continue
                    s[i] = c
                    break
        return "".join(s)
        
        ans = ''
        for i, c in enumerate(s):
            if c != '?':
                ans += c
                continue
            for t in string.ascii_letters:
                if ans and ans[-1] == t:
                    continue
                if i + 1 < len(s) and s[i + 1] == t:
                    continue
                ans += t
                break
        return ans