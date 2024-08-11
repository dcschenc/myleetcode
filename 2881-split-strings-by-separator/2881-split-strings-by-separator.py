class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        # for w in words:
        #     prev, i, n = 0, 0, len(w)
        #     while i < n:
        #         if w[i] == separator:
        #             if i - prev > 0:
        #                 ans.append(w[prev:i])
        #             prev = i + 1
        #         i += 1
        #     if i - prev > 0:
        #         ans.append(w[prev:i])
        # return ans

        for w in words:
            for s in w.split(separator):
                if s != '':
                    ans.append(s)
        return ans
