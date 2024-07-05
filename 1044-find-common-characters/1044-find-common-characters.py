class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hm = {}
        for c in words[0]:
            hm[c] = 1 + hm.get(c, 0)
        for word in words[1:]:
            for k, v in hm.items():
                if k not in word:
                    hm[k] = 0
                    # del hm[k]
                else:
                    count = word.count(k)
                    hm[k] = min(v, count)
  
        res = []
        for k, v in hm.items():
            if v > 0:
                for i in range(v):
                    res.append(k)
        return res
