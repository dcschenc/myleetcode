class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2410.Maximum%20Matching%20of%20Players%20With%20Trainers
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        p, t, ans, m, n = 0, 0, 0, len(players), len(trainers)
        while p < m and t < n:
            if players[p] <= trainers[t]:
                ans += 1
                p += 1
                t += 1
            else:
                p += 1
        return ans