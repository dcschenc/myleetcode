class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans = ''
        for d in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(d):
                if s[i] == d[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(d):
                if len(ans) < len(d):
                    ans = d
                elif len(ans) == len(d):
                    if d < ans:
                        ans = d
                    # for k in range(len(d)):
                    #     if d[k] == ans[k]:
                    #         continue
                    #     else:
                    #         if d[k] < ans[k]:
                    #             ans = d
                    #         break
        return ans
            