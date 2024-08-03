# from collections import Counter
class Solution:
    def greatestLetter(self, s: str) -> str:
        ss = set(s)
        for c in ascii_uppercase[::-1]:
            if c in ss and c.lower() in ss:
                return c
        return ''
        
        # seen = set()
        # for c in s:
        #     seen.add(c)
        # diff = ord('A') - ord('a')
        # i = ord('Z')
        # while i >= ord('A'):
        #     if chr(i) in seen and  chr(i - diff) in seen:
        #         return chr(i)
        #     i = i-1
        # return ''