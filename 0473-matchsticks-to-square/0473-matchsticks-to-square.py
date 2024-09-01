class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(i):
            if i == len(matchsticks):
                return s[0] == s[1] == s[2] == s[3]                  
                   
                
            for j in range(4):   
                if s[j] + matchsticks[i] > target:
                    continue     
                s[j] += matchsticks[i]   
                if dfs(i + 1): 
                    return True
                s[j] -= matchsticks[i]               
            return False

        s = [0 for i in range(4)]
        matchsticks.sort(reverse=True)
        target = sum(matchsticks)//4
        if target * 4 != sum(matchsticks):
            return False
        ans = dfs(0)        
        return ans