class Solution:
    def punishmentNumber(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2698.Find%20the%20Punishment%20Number%20of%20an%20Integer
        def dfs(s, target) -> bool :
            if len(s) == 0 and target == 0 :
                return True
            if target < 0 :
                return False
            ans = False 

            for i in range(len(s)) :
                left_part = s[0:i+1]
                right_part = s[i+1:]
                if dfs(right_part , target - int(left_part)):
                    return True
            return ans            
        
        total = 0
        for i in range(1, n+1) :
            square_n = i ** 2
            if dfs(str(square_n), i):
                total += square_n
        return total