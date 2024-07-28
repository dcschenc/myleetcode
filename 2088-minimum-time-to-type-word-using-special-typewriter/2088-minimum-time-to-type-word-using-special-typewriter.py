class Solution:
    def minTimeToType(self, word: str) -> int:
        word = 'a' + word       
        ans = 0
        for i in range(len(word)-1):            
            diff = abs(ord(word[i+1]) - ord(word[i]))         
            if diff <= 13:
                ans += diff
            else:
                ans += (26 - diff)
            ans += 1
        return ans