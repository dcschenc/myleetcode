class Solution:
    def maximumLengthSubstring(self, s: str) -> int:     
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3090.Maximum%20Length%20Substring%20With%20Two%20Occurrences
        cnt = Counter()
        ans = i = 0
        for j, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 2:
                cnt[s[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans

        n = len(s)
        mx = 0
        for i in range(n):
            counter = Counter()
            for j in range(i, n):
                counter[s[j]] += 1
                if counter[s[j]] > 2:
                    break
                mx = max(mx, j - i + 1)
        return mx
