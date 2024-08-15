class Solution:
    def minimumPushes(self, word: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3016.Minimum%20Number%20of%20Pushes%20to%20Type%20Word%20II
        counter = Counter(word)
        cur, ans = 1, 0
        for k, v in sorted(counter.items(), key=lambda x:x[1], reverse=True):
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