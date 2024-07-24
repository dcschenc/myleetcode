class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain,initial=0))
        max_alt, cur = 0, 0
        for v in gain:
            cur += v
            max_alt = max(max_alt, cur)
            # if curr > max_alt:
            #     max_alt = curr
        return max_alt
        