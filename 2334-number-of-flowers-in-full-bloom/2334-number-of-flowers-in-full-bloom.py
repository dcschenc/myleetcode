class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2251.Number%20of%20Flowers%20in%20Full%20Bloom
        # start, end = sorted(a for a, _ in flowers), sorted(b for _, b in flowers)
        # return [bisect_right(start, p) - bisect_left(end, p) for p in people]

        flowers.sort()
        sorted_people = sorted(people)
        ans = {}
        heap = []
        
        i = 0
        for person in sorted_people:
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                i += 1
            
            while heap and heap[0] < person:
                heapq.heappop(heap)
            
            ans[person] = len(heap)

        return [ans[x] for x in people]