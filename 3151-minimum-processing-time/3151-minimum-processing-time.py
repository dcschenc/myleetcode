class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2895.Minimum%20Processing%20Time
        processorTime.sort()
        tasks.sort()
        ans = 0
        i = len(tasks) - 1
        for t in processorTime:
            ans = max(ans, t + tasks[i])
            i -= 4
        return ans
        
        processorTime.sort()
        tasks.sort(reverse=True)
        ans, cu = 0, 0
        for p in processorTime:
            # for i in range(cur, 4 * n):
            ans = max(ans, tasks[cur] + p)
            cur += 4
        return ans

        # for p in processorTime:
        #     for i in range(cur, 4 * n):
        #         ans = max(ans, tasks[i] + p)
        #     cur += 4
        # return ans