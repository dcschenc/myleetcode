class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:        
        sorted_scores = sorted(score, reverse=True)
        # print(sorted_scores)
        hm = {}
        for i, v in enumerate(sorted_scores):
            hm[v] = i
        ans = []
        for v in score:
            if hm[v] == 0:
                ans.append('Gold Medal')
            elif hm[v] == 1:
                ans.append('Silver Medal')
            elif hm[v] == 2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(hm[v] +  1))
        return ans
