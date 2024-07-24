class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1737.Change%20Minimum%20Characters%20to%20Satisfy%20One%20of%20Three%20Conditions
        def f(cnt1, cnt2):
            for i in range(1, 26):
                t = sum(cnt1[i:]) + sum(cnt2[:i])
                nonlocal ans
                ans = min(ans, t)

        m, n = len(a), len(b)
        cnt1 = [0] * 26
        cnt2 = [0] * 26
        for c in a:
            cnt1[ord(c) - ord('a')] += 1
        for c in b:
            cnt2[ord(c) - ord('a')] += 1
        ans = m + n
        for c1, c2 in zip(cnt1, cnt2):
            ans = min(ans, m + n - c1 - c2)
        f(cnt1, cnt2)
        f(cnt2, cnt1)
        return ans

        cnt1, cnt2 = Counter(a), Counter(b)
        t1 = t2 = 0
        keys1, keys2 = sorted(cnt1.keys()), sorted(cnt2.keys())
        for k2 in keys2:
            if keys1[-1] >= k2:
                t1 += cnt2[k2]
        for k1 in keys1:
            if keys2[-1] >= k1:
                t2 += cnt1[k1]
        t3 = len(a) - max(cnt1.values()) + len(b) - max(cnt2.values())
        print(t1, t2, t3)
        return min(t1, t2, t3)


        for c1 in string.ascii_lowercase:
            flag = False
            if c1 in cnt2:
                for c2 in string.ascii_lowercase:
                    if c2 >= c1 and c2 in cnt1: 
                        t1 += cnt1[c2]
                        flag = True
            
            break
        t2 = 0
        for c1 in string.ascii_lowercase:
            if c1 in cnt1:
                for c2 in string.ascii_lowercase:
                    if c2 >= c1 and c2 in cnt2:
                        t2 += cnt2[c2]
                break
        