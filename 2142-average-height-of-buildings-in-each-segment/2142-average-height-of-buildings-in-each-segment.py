class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2015.Average%20Height%20of%20Buildings%20in%20Each%20Segment
        # Create dictionaries to track the total height and count of buildings at each point.
        total_height = defaultdict(int)
        building_count = defaultdict(int)
      
        # Iterate over each building's start and end points and update heights and counts.
        for start, end, height in buildings:
            building_count[start] += 1
            building_count[end] -= 1
            total_height[start] += height
            total_height[end] -= height
      
        # Initialize the result list and variables to store the running tally.
        result = []
        current_position = 0
        running_height = 0
        running_count = 0
      
        # Iterate over the sorted keys of the count dictionary.
        for position in sorted(building_count.keys()):
            # If there's at least one building in the current running range,
            # Calculate the average height and add it to the result list.
            if running_count:
                average_height = running_height // running_count
                new_interval = [current_position, position, average_height]
              
                # If the current interval can be merged with the last one in the result list,
                # Extend the last interval. Otherwise, add the new interval to the result list.
                if result and result[-1][1] == current_position and result[-1][2] == average_height:
                    result[-1][1] = position
                else:
                    result.append(new_interval)
          
            # Update the current position and the running tallies for the height and count.
            current_position = position
            running_height += total_height[position]
            running_count += building_count[position]
      
        return result
        
        height = defaultdict(int)
        cnt = defaultdict(int)
        for s, e, h in buildings:
            cnt[s] += 1
            cnt[e] -= 1
            height[s] += h
            height[e] -= h
        ans = []
        i = h = n = 0
        for j in sorted(cnt.keys()):
            if n:
                t = [i, j, h // n]
                if ans and ans[-1][1] == i and ans[-1][2] == t[-1]:
                    ans[-1][1] = j
                else:
                    ans.append(t)
            i = j
            h += height[j]
            n += cnt[j]
        return ans

        # points = []
        # for l, r, _ in buildings:
        #     points.append(l)
        #     points.append(r)
        # points.sort()
        # ans, n = [], len(points)
        # for i in range(2, n):
        #     l, r = points[i-1], points[i]


        