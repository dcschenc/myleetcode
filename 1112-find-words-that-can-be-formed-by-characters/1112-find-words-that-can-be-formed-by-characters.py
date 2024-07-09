# from collections import defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            if all(cnt[c] >= v for c, v in wc.items()):
                ans += len(w)
        return ans


        # chars_hm = defaultdict(int)
        # for c in chars:
        #     chars_hm[c] += 1
        # res = 0
        # for word in words:
        #     tmp_hm = chars_hm.copy()
        #     for i, c in enumerate(word):
        #         if tmp_hm[c] == 0:
        #             break
        #         if c in tmp_hm:
        #             tmp_hm[c] -= 1
                
        #         if i == len(word) - 1:
        #             res += len(word) 
        # return res