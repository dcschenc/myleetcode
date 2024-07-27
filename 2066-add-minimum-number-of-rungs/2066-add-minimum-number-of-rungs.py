class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1936.Add%20Minimum%20Number%20of%20Rungs
        cnt = 0
        i, n = 0, len(rungs)
        prev = 0
        while i < n:
            if prev + dist >= rungs[i]:
                prev = max(prev, rungs[i])
                i += 1                
            else:
                cnt += (rungs[i] - prev ) // dist - 1
                if (rungs[i] - prev) % dist != 0:
                    cnt += 1                   
                prev = rungs[i]
        return cnt
