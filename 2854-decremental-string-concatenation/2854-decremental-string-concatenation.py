class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2746.Decremental%20String%20Concatenation
        @cache
        def dp(i, a, b):
            if i == n:  
                return 0
            left = dp(i + 1, words[i][0], b)
            if words[i][-1] == a:
                left -= 1                
            right = dp(i + 1, a, words[i][-1])
            if words[i][0] == b:
                right -= 1
            return len(words[i]) + min(left, right)  

        n = len(words)   
        return len(words[0]) + dp(1, words[0][0], words[0][-1])

        # n = len(words)
        # dp = [0] * n
        # prev = words[0]
        # for i in range(1, n):
        #     if words[i][-1] == prev[0]:
        #         prev = words[i] + prev[1:]
        #     elif words[i][0] == prev[-1]:
        #         prev = prev + words[i][1:]
        #     else:
        #         prev = words[i] + prev
        # return len(prev)
