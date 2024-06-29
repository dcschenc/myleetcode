class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # https://leetcode.com/problems/fruit-into-baskets/description/
        cnt = Counter()
        ans = j = 0
        for i, x in enumerate(fruits):
            cnt[x] += 1
            while len(cnt) > 2:
                y = fruits[j]
                cnt[y] -= 1
                if cnt[y] == 0:
                    cnt.pop(y)
                j += 1
            ans = max(ans, i - j + 1)
        return ans


        n = len(fruits)
        i, l, mx = 0, 0, 0
        hm = defaultdict(int)
        while i < n:
            t = fruits[i]
            if t not in hm and len(hm) == 2:
                f, p = sorted(hm.items(), key=lambda x: x[1])[0]
                l = p + 1
                del hm[f]                
            hm[t] = i
            mx = max(mx, i - l + 1)
            i += 1
        return mx