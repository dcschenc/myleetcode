class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2135.Count%20Words%20Obtained%20After%20Adding%20a%20Letter
        hm = defaultdict(set)
        for w in startWords:
            w = ''.join(sorted(w))
            hm[len(w)].add(w)
        ans = 0
        for w1 in targetWords:
            w1 = ''.join(sorted(w1))
            candidates = hm[len(w1) - 1]
            for i in range(len(w1)):
                if w1[:i] + w1[i+1:] in candidates:
                    ans += 1
                    break
        return ans 
        