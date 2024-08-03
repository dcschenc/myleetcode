class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:        
        potions.sort()
        n = len(potions)
        ans = []
        for i in range(len(spells)):
            target = math.ceil(success/spells[i])
            idx = bisect_left(potions, target)
            ans.append(n - idx)
        return ans
