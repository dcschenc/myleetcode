class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ans, mx = -1, 0
        for i, (id, end) in enumerate(logs):
            if i == 0:
                start = 0
            else:
                start = logs[i-1][1]
            if end - start  > mx:
                mx = end - start
                ans = id
            elif end - start == mx and ans > id:
                ans = id
        return ans