from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0763.Partition%20Labels
        last = {c: i for i, c in enumerate(s)}
        mx = j = 0
        ans = []
        for i, c in enumerate(s):
            mx = max(mx, last[c])
            if mx == i:
                ans.append(i - j + 1)
                j = i + 1
        return ans
        
        hm = defaultdict(list)
        for i, c in enumerate(s):
            hm[c].append(i)
        parts = []
        i = 0
        while i < len(s):
            max_idx = hm[s[i]][-1]
            j = i + 1
            while j <= max_idx:
                cur = s[j]
                max_idx = max(max_idx, hm[cur][-1])
                j += 1
            # print(j, i)
            parts.append(max_idx-i+1)
            i = j
        return parts