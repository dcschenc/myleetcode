class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3025.Find%20the%20Number%20of%20Ways%20to%20Place%20People%20I
        def check(x1, x2, y1, y2):
            for x, y in points:
                if x == x1 and y == y1 or x == x2 and y == y2: 
                    continue
                if x1 <= x <= x2 and y2 <= y <= y1:
                    return False
            return True

        points.sort(key=lambda x: (x[0], -x[1]))
        n = len(points)
        cnt = 0
        # for (x1, y1), (x2, y2) in pairwise(points):        
        for (x1, y1), (x2, y2) in permutations(points, 2):    
            if x1 > x2 or y2 > y1: continue
            if check(x1, x2, y1, y2):              
                cnt += 1
        return cnt