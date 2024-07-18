class Solution:
    def numSub(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1513.Number%20of%20Substrings%20With%20Only%201s
        ans = cnt = 0
        for c in s:
            if c == "1":
                cnt += 1
            else:
                cnt = 0
            ans += cnt
        return ans % (10**9 + 7)    
        
        mod = 10**9 + 7
        i, n = 0, len(s)
        left = -1
        ans = 0
        while i < n:
            if s[i] == '1':
                left = i
                while i+1 < n and s[i+1] == '1':
                    i += 1
            if left != -1:
                cnt = i - left + 1
                ans += cnt * (cnt+1)//2
            left = -1
            i += 1
        return ans % mod