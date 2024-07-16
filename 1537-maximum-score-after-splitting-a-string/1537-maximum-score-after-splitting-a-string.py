class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        zeros = 0
        ans = 0 

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones -= 1
            else:
                zeros += 1
        
            ans = max(ans, zeros + ones)
        
        return ans

        return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))

        # presum = [0] * len(s)
        # total_1 = s.count('1')
        # ans = 0
        # for i in range(len(s)):
        #     if i > 0:
        #         presum[i] = presum[i-1]
        #     if s[i] == '1':
        #         presum[i] += 1
        # zeros = 0
        # for i in range(1, len(s)):
        #     if s[i-1] == '0':
        #         zeros  += 1
        #     ans = max(ans, zeros + total_1 - presum[i-1])
        # return ans