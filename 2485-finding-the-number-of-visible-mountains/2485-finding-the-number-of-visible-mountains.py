class Solution:
# https://algo.monster/liteproblems/2345
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2345.Finding%20the%20Number%20of%20Visible%20Mountains
        # Convert each peak to a representation of its visibility range (left and right points)
        visibility_ranges = [(x - y, x + y) for x, y in peaks]
      
        # Count how many times each visibility range occurs
        counts = Counter(visibility_ranges)
      
        # Sort the visibility ranges by the left point, and then by the right point in descending order
        visibility_ranges.sort(key=lambda point: (point[0], -point[1]))
      
        # Initialize the answer as 0 and the marker for the furthest right point seen so far as -infinity
        visible_mountains_count, furthest_right = 0, -inf
      
        # Loop through the sorted visibility ranges 
        for left, right in visibility_ranges:
            # If the right point of the current range is not further than the furthest right seen
            # it means this mountain is obscured by another, so we can continue
            if right <= furthest_right:
                continue
          
            # Update the furthest right point seen so far to the current range's right point
            furthest_right = right
          
            # If the current range only has one occurrence, it means the mountain is visible
            if counts[(left, right)] == 1:
                visible_mountains_count += 1
      
        # Return the total count of visible mountains
        return visible_mountains_count

        # stack = [-inf]
        # curMax = 0
        # for x, y in sorted(peaks):
		# 	# find slope
        #     pos, neg = x-y, x+y 			
		# 	# remove previous mountain that got overlapped
        #     while stack[-1] >= pos: 
        #         stack.pop()			
		# 	# will not get overlapped by previous mountain
        #     if neg > curMax: 
        #         curMax = neg 
        #         stack.append(pos)
        # return len(stack) - 1