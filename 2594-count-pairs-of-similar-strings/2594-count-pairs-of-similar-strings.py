class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # ans = 0
        # for a, b in combinations(words, 2):
        #     if set(a) == set(b):
        #         ans += 1
        # return ans
        
        # https://algo.monster/liteproblems/2506
        # bit mask
        ans = 0
        cnt = Counter()
        for w in words:
            v = 0
            for c in w:
                v |= 1 << (ord(c) - ord("A"))
            ans += cnt[v]
            cnt[v] += 1
        return ans