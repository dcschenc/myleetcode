class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()
        jobs = sorted(zip(difficulty, profit))
        ans = mx = i = 0
        for w in worker:
            while i < len(jobs) and jobs[i][0] <= w:
                mx = max(mx, jobs[i][1])
                i += 1
            ans += mx
        return ans
        
        n, m = len(difficulty), len(worker)
        work_profit = list(zip(difficulty, profit))
        work_profit.sort(key=lambda x: x[0])
        cur = work_profit[0][1]
        wp = [work_profit[0]]
        for i in range(1, n):
            if work_profit[i][1] > cur:
                cur = work_profit[i][1]
                wp.append(work_profit[i])

        works = [x[0] for x in wp]
        ans = 0
        for w in worker:
            idx = bisect_right(works, x=w)
            if idx - 1 >= 0:
                ans += wp[idx-1][1]
        return ans