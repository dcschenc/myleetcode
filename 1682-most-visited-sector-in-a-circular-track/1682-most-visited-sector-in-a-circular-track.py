class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        cnt = Counter()
        m = len(rounds)
        for i in range(m-1):
             j = rounds[i]
             while j != rounds[i+1]:
                cnt[j] += 1
                j += 1
                if j == n + 1:
                    j = 1
        cnt[rounds[m-1]] += 1
        mx = max(cnt.values())
        ans = [k for k, v in cnt.items() if v == mx]
        ans.sort()
        return  ans