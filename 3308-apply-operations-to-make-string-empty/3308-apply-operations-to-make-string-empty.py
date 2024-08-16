class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3039.Apply%20Operations%20to%20Make%20String%20Empty
        cnt = Counter(s)
        mx = cnt.most_common(1)[0][1]
        last = {c: i for i, c in enumerate(s)}
        return "".join(c for i, c in enumerate(s) if cnt[c] == mx and last[c] == i)

        counter = Counter(s)
        mx = max(counter.values())
        keys = [k for k, v in counter.items() if v == mx]
        idx = []
        for k in keys:
            i = len(s) - 1
            while s[i] != k:
                i -= 1
            idx.append(i)
        idx.sort()
        ans = ''
        for i in idx:
            ans += s[i]
        return ans