class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seen = False
        for i in range(len(s)):
            if s[i] == '1':
                if seen == True and i > 1 and s[i-1] == '0':
                    return False
                seen = True
        return True