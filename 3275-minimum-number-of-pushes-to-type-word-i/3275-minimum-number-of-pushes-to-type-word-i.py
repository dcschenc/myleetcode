class Solution:
    def minimumPushes(self, word: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3014.Minimum%20Number%20of%20Pushes%20to%20Type%20Word%20I
        n = len(word)
        ans, k = 0, 1
        for _ in range(n // 8):
            ans += k * 8
            k += 1
        ans += k * (n % 8)
        return ans

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
