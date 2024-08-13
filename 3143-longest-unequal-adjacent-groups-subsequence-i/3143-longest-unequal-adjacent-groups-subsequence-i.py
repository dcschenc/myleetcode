from itertools import product
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2900.Longest%20Unequal%20Adjacent%20Groups%20Subsequence%20I
        ans, prev = [], -1
        for w, g in zip(words, groups):
            if g != prev:
                ans.append(w)
                prev = g
        return ans