from collections import defaultdict
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        ans = 0
        max_defense = 0
        for _, defense in properties[::-1]:
            if max_defense > defense:
                ans += 1
            max_defense = max(max_defense, defense)
        return ans
       
    