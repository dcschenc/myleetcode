class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        while i < m and j < n:
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                ans.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            elif firstList[i][1] == secondList[j][1]:
                i += 1
                j += 1
            else:
                j += 1
        return ans