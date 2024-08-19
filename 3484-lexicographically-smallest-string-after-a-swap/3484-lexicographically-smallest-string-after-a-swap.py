class Solution:
    def getSmallestString(self, s: str) -> str:
        ss = [int(c) for c in s]
        n = len(ss)
        for i in range(n - 1):
            if ss[i] % 2 == 0 and ss[i + 1] % 2 == 0 or ss[i] % 2 == 1 and ss[i + 1] % 2 == 1:
                if ss[i] > ss[i + 1]:
                    ss[i], ss[i + 1] = ss[i + 1], ss[i]
                    break
        return ''.join([str(d) for d in ss])