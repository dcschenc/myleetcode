class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        d = ["ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"]
        hm = {}
        for i, s in enumerate(d, start=1):
            for c in s:
                hm[c] = i
        n = len(word)
        ans = 0
        for i in range(n):
            total = hm[word[i]]
            ans += 1
            for j in range(i + 1, n):
                total += hm[word[j]]
                if total % (j - i + 1) == 0:
                    ans += 1
        return ans
            