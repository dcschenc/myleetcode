class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        m, n = len(s), len(words)
        if m != n:
            return False
        for i in range(m):
            if s[i] != words[i][0]:
                return False
        return True
        