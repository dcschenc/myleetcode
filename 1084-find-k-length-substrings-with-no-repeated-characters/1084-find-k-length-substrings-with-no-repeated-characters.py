class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/
        
        cnt = Counter(s[:k])
        ans = int(len(cnt) == k)
        for i in range(k, len(s)):
            cnt[s[i]] += 1
            cnt[s[i - k]] -= 1
            if cnt[s[i - k]] == 0:
                cnt.pop(s[i - k])
            ans += int(len(cnt) == k)
        return ans

        # ans, n = 0, len(s)
        # l, i = 0, 0
        # hm = defaultdict(int)
        # while i < n:
        #     if s[i] in hm:
        #         if hm[s[i]] >= l:
        #             l = hm[s[i]] + 1
        #     hm[s[i]] = i
        #     if i - l + 1 == k:
        #         ans += 1
        #         l += 1
        #     i += 1
        # return ans