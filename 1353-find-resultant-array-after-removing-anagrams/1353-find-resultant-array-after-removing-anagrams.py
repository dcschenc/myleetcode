class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [w for i, w in enumerate(words) if i == 0 or sorted(w) != sorted(words[i - 1])]
        
        # ans = []
        # prev_key = -1
        # for i, w in enumerate(words):
        #     key = tuple(sorted(Counter(w).items()))
        #     if key != prev_key:
        #         ans.append(w)
        #     prev_key = key
        # return ans

        # ans = []
        # for i, w in enumerate(words):
        #     key = tuple(sorted(Counter(w).items()))
        #     if hm[key] == i:
        #         ans.append(w)
        # return ans