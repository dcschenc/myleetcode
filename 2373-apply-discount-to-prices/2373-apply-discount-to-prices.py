class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ans, s = '', sentence
        i, n = 0, len(s)
        for w in s.split():
            if w[0] == '$' and len(w) > 1 and all(c.isdigit() for c in w[1:]):
                ans += '$' + '{:.2f}'.format(int(w[1:]) * (100 - discount) / 100) + ' '
            else:
                ans += w + ' '
        return ans[:-1]