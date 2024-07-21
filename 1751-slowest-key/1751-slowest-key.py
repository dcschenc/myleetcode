class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        # hm = defaultdict(int)
        mx, mc = -1, ''
        for i, (t, c) in enumerate(zip(releaseTimes, keysPressed)):
            if i == 0:
                mx = t
                mc = c
            else:
                if mx < t - releaseTimes[i-1]:
                    mx = t - releaseTimes[i-1]
                    mc = c
                elif mx == t - releaseTimes[i-1] and mc < c:
                    mc = c
        return mc

        