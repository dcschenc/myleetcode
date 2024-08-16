class Solution:
    def numberCount(self, a: int, b: int) -> int:
        ans = 0
        for x in range(a, b + 1):
            x = str(x)
            cnt = Counter(x)
            if max(cnt.values()) < 2:
                ans += 1
        return ans