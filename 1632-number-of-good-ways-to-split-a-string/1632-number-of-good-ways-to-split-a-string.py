class Solution:
    def numSplits(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1525.Number%20of%20Good%20Ways%20to%20Split%20a%20String
        cnt = Counter(s)
        left = set()
        ans = 0
        for c in s:
            left.add(c)
            cnt[c] -= 1
            if cnt[c] == 0:
                cnt.pop(c)
            ans += len(left) == len(cnt)
        return ans


        i, n = 0, len(s)
        right = Counter(s)
        left = set()
        ans = 0
        for i in range(n):
            left.add(s[i])
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            if len(left) == len(right):
                ans += 1
        return ans

        prefix, hm = [], set()
        for c in s:
            hm.add(c)
            prefix.append(len(hm))
        postfix, hm = [0], set()
        for c in s[::-1]:
            hm.add(c)
            postfix.append(len(hm))
        n = len(s)
        ans = 0
        prefix = prefix[:-1]
        postfix = postfix[:-1]
        postfix.reverse()
        for i in range(n-1):
            if prefix[i] == postfix[i]:
                ans += 1
        return ans