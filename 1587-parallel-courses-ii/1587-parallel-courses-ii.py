from collections import defaultdict, deque
import itertools
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1494.Parallel%20Courses%20II
        d = [0] * (n + 1)
        for x, y in relations:
            d[y] |= 1 << x
        q = deque([(0, 0)])
        vis = {0}
        while q:
            cur, t = q.popleft()
            if cur == (1 << (n + 1)) - 2:
                return t
            nxt = 0
            for i in range(1, n + 1):
                if (cur & d[i]) == d[i]:
                    nxt |= 1 << i
            nxt ^= cur
            if nxt.bit_count() <= k:
                if (nxt | cur) not in vis:
                    vis.add(nxt | cur)
                    q.append((nxt | cur, t + 1))
            else:
                x = nxt
                while nxt:
                    if nxt.bit_count() == k and (nxt | cur) not in vis:
                        vis.add(nxt | cur)
                        q.append((nxt | cur, t + 1))
                    nxt = (nxt - 1) & x


        # Build the prerequisite graph
        prereq = [0] * n
        for u, v in relations:
            prereq[v-1] |= (1 << (u-1))
        
        # DP array
        dp = [float('inf')] * (1 << n)
        dp[0] = 0
        
        for mask in range(1 << n):
            available = []
            for i in range(n):
                if mask & (1 << i) == 0 and (mask & prereq[i]) == prereq[i]:
                    available.append(i)
                    
            # Generate all subsets of available courses
            for subset in itertools.combinations(available, min(k, len(available))):
                next_mask = mask
                for course in subset:
                    next_mask |= (1 << course)
                dp[next_mask] = min(dp[next_mask], dp[mask] + 1)
        
        return dp[(1 << n) - 1]