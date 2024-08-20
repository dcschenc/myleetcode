class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3259.Maximum%20Energy%20Boost%20From%20Two%20Drinks
        n = len(energyDrinkA)
        f = [[0] * 2 for _ in range(n)]
        f[0][0] = energyDrinkA[0]
        f[0][1] = energyDrinkB[0]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0] + energyDrinkA[i], f[i - 1][1])
            f[i][1] = max(f[i - 1][1] + energyDrinkB[i], f[i - 1][0])
        return max(f[n - 1])