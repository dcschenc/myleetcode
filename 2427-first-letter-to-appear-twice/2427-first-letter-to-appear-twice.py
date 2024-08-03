class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ss = set()
        for c in s:
            if c in ss:
                return c
            ss.add(c)