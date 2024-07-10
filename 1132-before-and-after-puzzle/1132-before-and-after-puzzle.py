from collections import defaultdict
from itertools import combinations
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        prefix_map = defaultdict(list)
        suffix_map = defaultdict(list)
        
        for i, phrase in enumerate(phrases):
            words = phrase.split()
            prefix_map[words[0]].append(i)
            suffix_map[words[-1]].append(i)
        
        result = set()
        
        for i, phrase in enumerate(phrases):
            words = phrase.split()
            prefix_candidates = suffix_map[words[0]]
            suffix_candidates = prefix_map[words[-1]]
            
            for j in prefix_candidates:
                if j != i:
                    result.add(phrases[j] + phrase[len(words[0]):])
            
            for k in suffix_candidates:
                if k != i:
                    result.add(phrase + phrases[k][len(words[-1]):])
        
        return sorted(list(result))


        # hm = {}
        # for i in range(len(phrases)):
        #     hm[i] = phrases[i].split(' ')
        # ans = set()
        # # for i in range(len(phrases)):
        # #     for j in range(i+1, len(phrases)):
        # for p1, p2 in list(combinations(phrases, 2)):
        #         # p1 = phrases[i]
        #         # p2 = phrases[j]
        #         arr1 = p1.split(' ')
        #         arr2 = p2.split(' ')
        #         # arr1 = hm[i]
        #         # arr2 = hm[j]
        #         if arr1[-1] == arr2[0]:
        #             if len(arr1) == 1:
        #                 ans.add(p2)
        #             else:
        #                 ans.add(' '.join(arr1[:-1]) + ' ' + p2)
        #         if arr1[0] == arr2[-1]:
        #             if len(arr2) == 1:
        #                 ans.add(p1)
        #             else:
        #                 ans.add(' '.join(arr2[:-1]) + ' ' + p1)
        # return sorted(ans)

        # prefix = defaultdict(list)
        # postfix = defaultdict(list)
        # for p in phrases:
        #     arr = p.split(' ')
        #     prefix[arr[0]].append(p)
        #     postfix[arr[-1]].append(p)
        # ans = set()
        # print(prefix, postfix)
        # for p in phrases:
        #     arr = p.split(' ')
        #     print(arr, prefix[arr[-1]], postfix[arr[0]])
        #     if arr[-1] in prefix:
        #         for p2 in prefix[arr[-1]]:    
        #             new = (' '.join(arr[:-1]) + ' ' + p2).strip()
        #             ans.add(new)
        #     if arr[0] in postfix:
        #         for p2 in postfix[arr[0]]:
        #             new = (p2 + ' ' + ' '.join(arr[1:])).strip()
        #             ans.add(new)
        
        # return sorted(ans)