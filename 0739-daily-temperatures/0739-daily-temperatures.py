class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:     
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0739.Daily%20Temperatures   
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack != [] and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1] 
                stack.pop()            
            stack.append(i)
        return res