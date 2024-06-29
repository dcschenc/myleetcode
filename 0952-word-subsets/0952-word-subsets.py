class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0916.Word%20Subsets
        cnt = Counter()
        for b in words2:
            t = Counter(b)
            for c, v in t.items():
                cnt[c] = max(cnt[c], v)
                
        ans = []
        for a in words1:
            t = Counter(a)
            if all(v <= t[c] for c, v in cnt.items()):
                ans.append(a)
        return ans

