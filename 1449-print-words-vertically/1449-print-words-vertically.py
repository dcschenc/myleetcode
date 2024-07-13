class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        words = s.split(' ')
        n = max([len(w) for w in words])
        for i in range(n):
            cur = ''
            for word in words:
                if i < len(word):
                    cur += word[i]
                else:
                    cur += ' '
            cur = cur.rstrip()
            ans.append(cur)
        return ans