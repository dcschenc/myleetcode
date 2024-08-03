class Solution:
# https://algo.monster/liteproblems/2345
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2345.Finding%20the%20Number%20of%20Visible%20Mountains
        arr = [(x - y, x + y) for x, y in peaks]
        cnt = Counter(arr)
        arr.sort(key=lambda x: (x[0], -x[1]))
        ans, cur = 0, -inf
        for l, r in arr:
            if r <= cur:
                continue
            cur = r
            if cnt[(l, r)] == 1:
                ans += 1
        return ans

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