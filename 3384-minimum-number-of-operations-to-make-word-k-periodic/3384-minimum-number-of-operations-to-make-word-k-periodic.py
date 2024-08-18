class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter()
        for i in range(0, n, k):
            cnt[word[i:i+k]] += 1
        # print(cnt)
        mx = max(cnt.values())
        c = ''
        for k, v in cnt.items():
            if v == mx:
                c = k
                break

        return sum(v for k, v  in cnt.items() if k != c)