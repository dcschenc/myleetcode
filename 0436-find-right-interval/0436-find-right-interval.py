class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # def binary_search(end):
        #     l, r = 0, len(starts) - 1
        #     while l < r:
        #         mid = (l+r)//2
        #         if starts[mid] == end:
        #             return starts[mid]
        #         elif starts[mid] > end:
        #             r = mid
        #         else:
        #             l = mid + 1
        #     return starts[l]

        hm = {}
        for i, (start, end) in enumerate(intervals):
            hm[start] = i
        ans = []
        starts = sorted(list(hm.keys()))
        for start, end in intervals:
            if starts[-1] < end:
                found = -1
            else:
                # start = binary_search(end)
                idx = bisect_left(starts, x=end)
                key = starts[idx]
                found = hm[key]
            # for i in range(len(starts)):
            #     if starts[i] >= end:
            #         found = hm[starts[i]]
            #         break
            ans.append(found)
        return ans


