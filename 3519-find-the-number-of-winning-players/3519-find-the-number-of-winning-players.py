class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = defaultdict(Counter)
        winners = set()
        for i, c in pick:
            cnt[i][c] += 1
            if cnt[i][c] > i:
                winners.add(i)
        return len(winners)