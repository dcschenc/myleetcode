from collections import Counter
class Solution:
    def numWays(self, s: str) -> int:        
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1573.Number%20of%20Ways%20to%20Split%20a%20String
        def find(x):
            t = 0
            for i, c in enumerate(s):
                t += int(c == '1')
                if t == x:
                    return i

        cnt, m = divmod(sum(c == '1' for c in s), 3)
        if m:
            return 0
        n = len(s)
        mod = 10**9 + 7
        if cnt == 0:
            return ((n - 1) * (n - 2) // 2) % mod
        i1, i2 = find(cnt), find(cnt + 1)
        j1, j2 = find(cnt * 2), find(cnt * 2 + 1)
        return (i2 - i1) * (j2 - j1) % (10**9 + 7)

        mod = 10 ** 9 + 7      
        num_1 = s.count('1')
        if num_1 == 0:
            return math.comb(len(s)-1, 2) % mod
        if num_1 % 3 != 0:
            return 0
        num_1 = num_1 // 3
        i = 0
        split = []
        cnt = 0
        while i < len(s):
            if s[i] == '1':
                cnt += 1                
            if cnt == num_1:
                split.append(1)
                j = i + 1
                while j < len(s) and s[j] != '1':
                    split[-1] += 1
                    j += 1
                cnt = 0          
                i = j
            else:                        
                i += 1
    
        ans = 1
        for p in split[:-1]:
            ans *= p
        return ans % mod



