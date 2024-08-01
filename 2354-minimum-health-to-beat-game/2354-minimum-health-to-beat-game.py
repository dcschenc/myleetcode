class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2214.Minimum%20Health%20to%20Beat%20Game
        return sum(damage) - min(max(damage), armor) + 1

        maxHealth = sum(damage) + 1
        maxBlocked = -1 

        for levelDamage in damage:
            if (levelDamage >= armor):
                return maxHealth - armor

            maxBlocked = max(maxBlocked, levelDamage)

        maxHealth -= maxBlocked

        return maxHealth