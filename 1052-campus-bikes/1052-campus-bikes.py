# from itertools import combination
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                w, b = workers[i], bikes[j]
                dist = abs(w[0] - b[0]) + abs(w[1] - b[1])
                distances.append((dist, i, j))
                
        distances.sort(key = lambda x: (x[0], x[1], x[2]))
        # print(distances)
        ans = [-1] * len(workers)
        used_bikes = set()
        for _, w, b in distances:
            if ans[w] == -1 and b not in used_bikes:
                ans[w] = b
                used_bikes.add(b)        
        return ans
