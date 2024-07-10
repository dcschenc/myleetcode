class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a, n = 0, len(distance)
        while start != destination:
            a += distance[start]
            start = (start + 1) % n
        return min(a, sum(distance) - a)
        
        # dist1, dist2 = 0, 0
        # n = len(distance)
        # i = start
        # while i != destination:
        #     dist1 += distance[i]
        #     i += 1
        #     i = i%n
        # i = start
        # while i != destination:
        #     i = i-1
        #     if i == -1:
        #         i = n-1
        #     dist2 += distance[i]
        # return min(dist1, dist2)