class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2531.Make%20Number%20of%20Distinct%20Characters%20Equal
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        x, y = len(cnt1), len(cnt2)
        for c1, v1 in cnt1.items():
            for c2, v2 in cnt2.items():
                if c1 == c2:
                    if x == y:
                        return True
                else:
                    # new number of chars in word1
                    a = x - (v1 == 1) + (cnt1[c2] == 0) 
                    # new number of chars in word2
                    b = y - (v2 == 1) + (cnt2[c1] == 0)
                    if a == b:
                        return True
        return False

        # cnt1, cnt2 = [0] * 26, [0] * 26
        # for c in word1:
        #     cnt1[ord(c) - ord('a')] += 1
        # for c in word2:
        #     cnt2[ord(c) - ord('a')] += 1
        # for i, c1 in enumerate(cnt1):
        #     for j, c2 in enumerate(cnt2):
        #         if c1 != 0 and c2 != 0:
        #             cnt1[i], cnt2[j] = cnt1[i] - 1, cnt2[j] - 1
        #             cnt1[j], cnt2[i] = cnt1[j] + 1, cnt2[i] + 1
        #             if sum([c > 0 for c in cnt2]) == sum([c > 0 for c in cnt1]):
        #                 return True
        #             cnt1[i], cnt2[j] = cnt1[i] + 1, cnt2[j] + 1
        #             cnt1[j], cnt2[i] = cnt1[j] - 1, cnt2[i] - 1
        # return False

        # hm1, hm2 = Counter(word1), Counter(word2)
        # if abs(len(hm1) - len(hm2)) > 3:
        #     return False      

        # if len(hm1) == len(hm2):
        #     single1 = any(v == 1 for k, v in hm1.items())
        #     single2 = any(v == 1 for k, v in hm2.items())
        #     if single1 and single2:
        #         return True
        #     multiple1 = any(v >=2 for k, v in hm1.items())
        #     multiple2 = any(v >=2 for k, v in hm2.items())
        #     if multiple1 and multiple2:
        #         return True
        #     return False

        # if len(hm2) > len(hm1):
        #     hm1, hm2 = hm2, hm1
        
        # if len(hm1) - len(hm2) == 1:
        #     print(hm1, hm2)
        #     for k1, v1 in hm1.items():
        #         if k1 not in hm2 and v1 >= 2:
        #             for k2, v2 in hm2.items():
        #                 if k2 != k1 and v2 >=2 and k2 in hm1:
        #                     return True
        # if len(hm1) - len(hm2) == 2:
        #     print(hm1, hm2)
        #     for k1, v1 in hm1.items():
        #         if k1 not in hm2 and v1 == 1:
        #             for k2, v2 in hm2.items():
        #                 if k2 != k1 and v2 > 1 and k2 in hm1:
        #                     return True
        # return False