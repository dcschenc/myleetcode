from collections import defaultdict, Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2083.Substrings%20That%20Begin%20and%20End%20With%20the%20Same%20Letter
        cnt = Counter()
        ans = 0
        for c in s:
            cnt[c] += 1
            ans += cnt[c]
        return ans
        
        # counter = Counter(s)
        # cnt = len(s)
        # for k, v in counter.items():        
        #     cnt += v * (v - 1)//2
        # return cnt