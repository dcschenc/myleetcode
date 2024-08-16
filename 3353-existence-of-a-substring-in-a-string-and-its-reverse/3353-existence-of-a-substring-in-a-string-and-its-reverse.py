class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        ss = set()
        n = len(s)
        for i in range(n-1):
            ss.add(s[i:i+2])

        for i in range(n-1, 0, -1):
            if s[i] + s[i-1] in ss:
                return True
        return False