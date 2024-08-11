class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2744.Find%20Maximum%20Number%20of%20String%20Pairs
        cnt = Counter()
        ans = 0
        for w in words:
            ans += cnt[w[::-1]]
            cnt[w] += 1
        return ans
        
        counter = Counter(words)
        ans = 0
        # print(counter)
        for k, c in counter.items():
            if k == k[::-1]:
                if c > 1:
                    ans +=  (c // 2) * 2
                continue
            if k[::-1] in counter:
                ans += min(c, counter[k[::-1]])
        return ans // 2