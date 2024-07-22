class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1657.Determine%20if%20Two%20Strings%20Are%20Close
        c1 = Counter(word1)
        c2 = Counter(word2)
        c1 = list(c1.values())
        c1.sort()
        c2 = list(c2.values())
        c2.sort()

        #### the numsers are the same, and character set are the same ####
        return  c1 == c2 and set(word1) == set(word2)