from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = (s1 + " " + s2).split()
        return [word for word, cnt in Counter(words).items() if cnt == 1]
        # res = defaultdict(int)
        # result = []
        # for w in words:
        #     res[w] += 1
        # for k, v in res.items():
        #     if v == 1:
        #         result.append(k)
        # return result