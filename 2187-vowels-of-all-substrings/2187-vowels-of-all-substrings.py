class Solution:
    def countVowels(self, word: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2063.Vowels%20of%20All%20Substrings
        # ans = 0
        # dp = 0
        # for i, c in enumerate(word):
        #     if c in "aeiou":
        #         dp += (i+1)
        #     ans += dp
        # return ans

        n = len(word)
        ans = 0
        for i, c in enumerate(word):
            if c in 'aeiou':
                ans += (i + 1) * (n - i)   # take or not take 
        return ans


        c, l = 0, len(word)
        # d = {'a':1, 'e':1,'i':1,'o':1,'u':1}
        d = 'aeiou'
        
        for i in range(l):
            if word[i] in d:
                c += (l-i)*(i+1)
        return c