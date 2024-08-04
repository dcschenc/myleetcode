class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans = 0
        while s.count('01'):
            s = s.replace('01', '10')
            ans += 1
        return ans
        
        cnt = 0
        while True:
            idx = s.find('01')
            if idx == -1:
                break
            s = s.replace('01', '10')            
            cnt += 1
        return cnt
            