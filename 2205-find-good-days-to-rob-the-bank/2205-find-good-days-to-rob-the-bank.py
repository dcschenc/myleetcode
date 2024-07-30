class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        result = []
        n = len(security)
        increasing = [0] * n
        decreasing = [0] * n        
        for i in range(1, n):
            if security[i] <= security[i-1]:
                decreasing[i] = decreasing[i-1] + 1
        for i in range(n-2, -1, -1):
            if security[i] <= security[i+1]:
                increasing[i] = increasing[i+1] + 1
        # print(decreasing, increasing)
        for i in range(n):
            if decreasing[i] >= time and increasing[i] >= time:
                result.append(i)
        return result