class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1229.Meeting%20Scheduler
        slots1.sort()
        slots2.sort()
        m, n = len(slots1), len(slots2)
        i = j = 0
        while i < m and j < n:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
        
        slots1.sort(key=lambda x: (x[0], -x[1]))
        slots2.sort(key=lambda x:(x[0], -x[1]))
        m, n = len(slots1), len(slots2)
        i, j = 0, 0
        while i < m and j < n:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            if start < end and end - start  >= duration:
                return [start, start + duration]
            else:
                if slots1[i][1] < slots2[j][1]:
                    i += 1
                elif slots1[i][1] > slots2[j][1]:
                    j += 1
                else:
                    if slots1[i][0] < slots2[j][0]:
                        i += 1
                    else:
                        j += 1
        return []