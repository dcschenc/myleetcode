class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3207.Maximum%20Points%20After%20Enemy%20Battles
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]:
            return 0
        ans = 0
        for i in range(len(enemyEnergies) - 1, -1, -1):
            ans += currentEnergy // enemyEnergies[0]
            currentEnergy %= enemyEnergies[0]
            currentEnergy += enemyEnergies[i]
        return ans