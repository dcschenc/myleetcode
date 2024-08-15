class Solution:
    def minimumPushes(self, word: str) -> int:
        # counter = Counter(word)
        cur, ans = 1, 0
        # for k, v in sorted(counter.items(), key=lambda x:x[1], reverse=True):
        for c in word:
            v = 1
            if cur <= 8:
                ans += v
            elif cur <= 16:
                ans += 2 * v
            elif cur <= 24:
                ans += 3 * v
            else:
                ans += 4 *v
            cur += 1
        return ans
