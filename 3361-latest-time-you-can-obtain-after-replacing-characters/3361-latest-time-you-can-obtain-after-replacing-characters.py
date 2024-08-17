class Solution:
    def findLatestTime(self, s: str) -> str:
        latest = '00:00'
        for i in range(12):
            for j in range(60):
                cur = '{:02}'.format(i) + ':' + '{:02}'.format(j)
                flag = True
                for k in range(5):
                    if s[k] != '?' and cur[k] != s[k]:
                        flag = False
                        break
                if flag:
                    latest = cur
        return latest
