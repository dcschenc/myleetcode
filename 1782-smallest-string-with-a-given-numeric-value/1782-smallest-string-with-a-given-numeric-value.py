class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1663.Smallest%20String%20With%20A%20Given%20Numeric%20Value
        s = ['a'] * n
        diff = k - n
        i = n - 1
        while diff > 0:
            if diff >= 25:
                s[i] = 'z'
                diff -= 25
            else:
                s[i] = chr(ord('a') + diff)
                break
            i -= 1
        return ''.join(s)

        # base = ord('a')
        # ans = ''
        # while k > n and n > 0:
        #     mod = (k - (n-1)) % 26
        #     cur = chr(mod + base - 1)
        #     ans += cur
        #     print(k, n)
        #     k -= mod            
        #     n -= 1
        # ans = ans + 'a' * n
        # return ans[::-1]
        