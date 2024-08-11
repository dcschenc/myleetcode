class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2747.Count%20Zero%20Request%20Servers
  
        logs.sort(key=lambda x: x[1])
        j = k = 0
        counter = Counter()
        ans = [0] * len(queries)
        for r, i in sorted(zip(queries, count())):
            l = r - x
            while k < len(logs) and logs[k][1] <= r:
                counter[logs[k][0]] += 1
                k += 1
            while j < len(logs) and logs[j][1] < l:
                counter[logs[j][0]] -= 1
                if counter[logs[j][0]] == 0:
                    counter.pop(logs[j][0])
                j += 1
            ans[i] = n - len(counter)
        return ans
