class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1347.Minimum%20Number%20of%20Steps%20to%20Make%20Two%20Strings%20Anagram
        cnt = Counter(s)
        ans = 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                ans += 1
        return ans

        counter1, counter2 = Counter(s), Counter(t)
        n = len(s)
        common = 0
        for k, v in counter2.items():
            if k in counter1:
                common += min(v, counter1[k])
        return n - common