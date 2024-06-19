from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm = defaultdict(int)
        for i in range(len(s)-10+1):
            hm[s[i:i+10]] += 1
        # print(hm)
        result = [s for s in hm if hm[s] > 1]
        return result