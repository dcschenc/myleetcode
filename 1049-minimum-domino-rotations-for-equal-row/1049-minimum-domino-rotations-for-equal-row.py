class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def swap():
            mx = Counter(tops).most_common(1)[0][0]
            ans = 0
            for t, b in zip(tops, bottoms):
                if t != mx:
                    if b != mx:
                        return -1
                    else:
                        ans += 1
            return ans

        ans_t = swap()
        tops, bottoms = bottoms, tops
        ans_b = swap()
        if ans_t == -1:
            return ans_b
        elif ans_b == -1:
            return ans_t
        return min(ans_t, ans_b)
        