class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1328.Break%20a%20Palindrome
        s = list(palindrome)
        n, i = len(s), 0
        mid = -1 if n % 2 == 0 else n //2
        i = 0
        while i < n:
            if mid != -1 and i == mid:
                i += 1
                continue

            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)
            elif i == n - 1:
                s[i] = 'b'               
                return ''.join(s)
            i += 1
        return ''