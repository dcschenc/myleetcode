class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2406.Divide%20Intervals%20Into%20Minimum%20Number%20of%20Groups
        intervals.sort(key=lambda x: (x[0], x[1]))       
        heaps = []
        ans = 0
        for i, (l, r) in enumerate(intervals):  
            if heaps and l > heaps[0]:
                heappop(heaps)                
            else:                
                ans += 1
            heappush(heaps, r)
        return ans

        # for i, groups in enumerate(hm):
        #     x, y = groups[-1]
        #     if l > y:
        #         hm[i].append((l, r))
        #         last_r = min(last_r, r)
        #         found = True
        #         break
        # if found is False:
        #     hm.append([[l, r]])

        