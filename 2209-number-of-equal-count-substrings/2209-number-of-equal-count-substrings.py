from collections import defaultdict
class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2067.Number%20of%20Equal%20Count%20Substrings
        ans = 0 
        for k in range(1, 27): 
            freq = Counter()
            uniq = 0 
            for i, ch in enumerate(s): 
                freq[ch] += 1
                if freq[ch] == count: 
                    uniq += 1
                if i >= k * count: 
                    if freq[s[i - k * count]] == count: 
                        uniq -= 1
                    freq[s[i - k * count]] -= 1                    
                if uniq == k: 
                    ans += 1
        return ans 
