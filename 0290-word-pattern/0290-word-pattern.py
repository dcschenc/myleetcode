class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        words = [x for x in words if x!=' ']
        # print(words)
        if len(words) != len(pattern):
            return False
        p2w = {}
        w2p = {}
        for i, c in enumerate(pattern):
            if c not in p2w:
                if words[i] not in w2p:
                    p2w[c] = words[i]
                    w2p[words[i]] = c
                else:
                    return False
            elif p2w[c] != words[i]:
                return False
        return True

        # hm2 = {}
        # for w in s:
        #     if w not in hm2:
        #         hm2[w] = 1
        #     else:
        #         hm2[w]+=1 
        
        # values1 = list(hm.values())
        # # values1.sort()
        # print(values1)
        # values2 = list(hm2.values())
        # # values2.sort()
        # print(values2)
        # return values1 == values2