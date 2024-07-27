class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1921.Eliminate%20Maximum%20Number%20of%20Monsters
        n = len(dist)
        arrives = []
        for d, s in zip(dist, speed):
            arrives.append(d / s)
        
        arrives.sort()
        ans = 0
        for i in range(n):
            if arrives[i] <= i:
                break
            ans += 1
        return ans
        

        # heap = []
        # for d, s in zip(dist, speed):
        #     heappush(heap, (d - s, s))
        # ans = 1
        # while heap:
        #     # d, s = heappop(heap)
        #     cnt = 0
        #     for d, s in 
