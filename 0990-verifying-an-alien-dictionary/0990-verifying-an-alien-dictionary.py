class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # https://leetcode.com/problems/verifying-an-alien-dictionary/editorial/
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):

            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

        def compare_word(word1, word2):           
            i = 0
            while i < len(word1) and i < len(word2):
                if hm[word1[i]] > hm[word2[i]]:
                    return False
                elif hm[word1[i]] < hm[word2[i]]:
                    return True
                i += 1
            if len(word1) > len(word2):
                return False            
            return True

        hm = {}
        for i in range(len(order)):
            hm[order[i]] = i
        
        for i in range(1, len(words)):
            if not compare_word(words[i-1], words[i]):
                return False
        return True
        