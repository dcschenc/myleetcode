from heapq import heappush, heappop
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        minheap = []
        for i, (p, t) in enumerate(classes):
            heappush(minheap, (p/t - (p + 1)/(t + 1), t, i))
        while extraStudents > 0:
            r, t, i = heappop(minheap)
            cur = classes[i]
            cur[0] += 1
            cur[1] += 1
            heappush(minheap, (cur[0]/cur[1] - (cur[0] + 1)/(cur[1] + 1), classes[i][1], i))
            extraStudents -= 1
        ans = 0
        for p, t in classes:
            ans += p / t
        return ans / n
        
        