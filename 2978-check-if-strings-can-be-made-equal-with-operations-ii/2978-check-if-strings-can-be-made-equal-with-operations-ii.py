class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2840.Check%20if%20Strings%20Can%20be%20Made%20Equal%20With%20Operations%20II
        n = len(s1)
        odd1, even1, odd2, even2 = '', '', '', ''
        for i in range(n):
            if i % 2 == 0:
                even1 += s1[i]
                even2 += s2[i]
            else:
                odd1 += s1[i]
                odd2 += s2[i]
                                
        return sorted(even1) == sorted(even2) and sorted(odd1) == sorted(odd2)