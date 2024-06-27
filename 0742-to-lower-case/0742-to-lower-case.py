class Solution:
    def toLowerCase(self, s: str) -> str:
        diff = ord('a') - ord('A')
        # s = list(s)
        res = ''
        for c in s:
            if ord('A') <=ord(c) <=ord('Z'):
                # print(ord(c)-diff)
                res += chr(ord(c)+diff)
            else:
                res += c
        return res