class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # cnt1 = Counter(s)
        # cnt2 = Counter(t)
        # for k in cnt2.keys():            
        #     if k not in cnt1 or cnt2[k] == cnt1[k] + 1:
        #         return k

        ch = 0
        for c in s + t:
            ch ^= ord(c)
        return chr(ch)
            