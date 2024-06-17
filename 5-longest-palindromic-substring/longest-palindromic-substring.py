class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, l, r):           
            nonlocal length
            nonlocal res
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    length = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

        length = 0
        res = ''
        for i in range(len(s)):            
            helper(s, i, i)
            helper(s, i, i + 1)
        return res




        def get_longest_palindromic(left, right):
            while left >=0 and right <=n-1 and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        n = len(s)
        longest = 0
        for i in range(n):
            length1 = get_longest_palindromic(i, i)
            length2 = get_longest_palindromic(i, i+1)
            length = max(length1, length2)
            if length > longest:
                longest = length
                left, right = i - (length-1)//2, i+length//2
        return s[left:right+1]
        
        # def get_longest_palindromic(i):
        #     k, l = i-1, i+1
        #     length = 1
        #     while k>=0 and l <= n-1 and s[k] == s[l]:
        #         k-=1
        #         l+=1
        #         length += 2
        #     if length == 1:
        #         if k>=0 and s[k] == s[i]:
        #             return 2, k, i
        #         if l <=n-1 and s[i] == s[l]:
        #             return 2, i, l
        #     # print(i, k, l)
        #     return length, k+1, l-1

        # n = len(s)
        # longest = 0
        # left, right = 0, 0
        # for i in range(n):
        #     length, k, l = get_longest_palindromic(i)
        #     print(i, length, k, l)
        #     if length > longest:
        #         longest = length
        #         left, right = k, l
        # return s[left:right+1]
        