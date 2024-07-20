class Solution:
    def modifyString(self, s: str) -> str:
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