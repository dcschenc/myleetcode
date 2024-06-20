class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 1
        end_points= [intervals[0][1]]
        for i in range(1, len(intervals)):
            found = False
            for j in range(len(end_points)):
                if end_points[j] <= intervals[i][0]:
                    end_points[j] = intervals[i][1]
                    found = True
                    break
            if found == False:
                # count += 1
                end_points.append(intervals[i][1])
           
        # return count
        return len(end_points)