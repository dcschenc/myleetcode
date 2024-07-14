class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1353.Maximum%20Number%20of%20Events%20That%20Can%20Be%20Attended

        # Create a default dictionary to hold events keyed by start date
        event_dict = defaultdict(list)
      
        # Initialize variables to track the earliest and latest event dates
        earliest_start, latest_end = inf, 0
      
        # Populate event_dict with events and update earliest_start and latest_end
        for start, end in events:
            event_dict[start].append(end)
            earliest_start = min(earliest_start, start)
            latest_end = max(latest_end, end)
      
        # Initialize an empty min-heap to store active events' end dates
        min_heap = []
      
        # Counter for the maximum number of events one can attend
        max_events_attended = 0
      
        # Iterate over each day within the range of event dates
        for day in range(earliest_start, latest_end + 1):
            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
          
            # Push all end dates of events starting today onto the heap
            for end in event_dict[day]:
                heappush(min_heap, end)
          
            # If there are any events available to attend today, attend one and increment count
            if min_heap:
                max_events_attended += 1
                heappop(min_heap)  # Remove the event that was attended
      
        # Return the total number of events attended
        return max_events_attended


        # ans, cur = 0, 0
        # events.sort(key=lambda x:(x[0], x[1]))
        # days = defaultdict(int)
        # print(events)
        # for s, e in events:
        #     print(cur, s, e)
        #     for d in range(max(cur+1, s), e+1):
        #         if days[d] == 0:
        #             days[d] = 1
        #             cur = d
        #             ans += 1
        #             break            
        # return ans

        # @cache
        # def dfs(i):
        #     if i >= len(events):
        #         return 0
        #     start, end = events[i]
        #     cnt = counter[(start, end)]
        #     j = bisect_left(events, end, lo = i + 1, key=lambda x: x[0])
        #     return max(cnt + dfs(j), dfs(i+1))
        # # events = list(set([(x[0], x[1]) for x in events]))
        # counter = defaultdict(int)
        # for start, end in events:
        #     counter[(start, end)] += 1
        # events.sort(key = lambda x: (x[0]))
        # return dfs(0)