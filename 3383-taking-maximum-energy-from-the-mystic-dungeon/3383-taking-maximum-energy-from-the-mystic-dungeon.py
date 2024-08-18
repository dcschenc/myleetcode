class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3147.Taking%20Maximum%20Energy%20From%20the%20Mystic%20Dungeon
        ans = -inf
        n = len(energy)
        for i in range(n - k, n):
            j, s = i, 0
            while j >= 0:
                s += energy[j]
                ans = max(ans, s)
                j -= k
        return ans