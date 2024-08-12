class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2839.Check%20if%20Strings%20Can%20be%20Made%20Equal%20With%20Operations%20I
        return set([s1[0], s1[2]]) == set([s2[0], s2[2]]) and set([s1[1], s1[3]]) == set([s2[1], s2[3]])