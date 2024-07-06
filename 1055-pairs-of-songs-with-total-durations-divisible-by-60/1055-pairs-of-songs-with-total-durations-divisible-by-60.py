class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hm = defaultdict(int)
        n = len(time)
        ans = 0
        for t in time:
            mod = t % 60
            if mod == 0:
                ans += hm[0]
            elif (60 - mod) in hm:
                ans += hm[60 - mod]
            hm[mod] += 1
        return ans
        