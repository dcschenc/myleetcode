class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def convert(w):
            return ''.join(['*' if c in 'aeiou' else c for c in w])

        m, n = len(wordlist), len(queries)
        ans = [''] * n
        low, vowels = {}, {}
        for w in wordlist:           
            t = w.lower()
            low.setdefault(t, w)            
            vowels.setdefault(convert(t), w)

        s = set(wordlist)
        for i, q in enumerate(queries):
            if q in s:
                ans[i] = q
                continue
            q = q.lower()
            if q in low:
                ans[i] = low[q]
            else:
                q = convert(q)
                if q in vowels:
                    ans[i] = vowels[q]                
        return ans

        # m, n = len(wordlist), len(queries)
        # ans = [''] * n
        # s = set(wordlist)
        # for i, q in enumerate(queries):
        #     if q in s:
        #         ans[i] = q
        #     else:
        #         found = False
        #         q = q.lower()
        #         for w in wordlist:                    
        #             if w.lower() == q:
        #                 found = True
        #                 ans[i] = w
        #                 break
        #         if not found:
        #             for j, w in enumerate(wordlist):
        #                 w = w.lower()                        
        #                 if len(w) == len(q) and all(c1 == c2 or (c1  in 'aeiou' and c2 in 'aeiou') for c1, c2 in zip(w, q)):
        #                     ans[i] = wordlist[j]
        #                     break
        # return ans

                 