from heapq import heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1834.Single-Threaded%20CPU
        tasks = sorted([(enqueue, processing, i) for i, (enqueue, processing) in enumerate(tasks)])
        heap = []
        current_time, result, i = 0, [], 0

        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= current_time:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            if heap:
                processing_time, task_index = heappop(heap)
                current_time += processing_time
                result.append(task_index)
            elif i < len(tasks):
                current_time = tasks[i][0]

        return result

        # hm = {}
        # for i in range(len(tasks)):
        #     hm[(tasks[i][0], tasks[i][1])] = i 
        # tasks.sort(key=lambda x:x[0])
        # # print(tasks)
        # minheap = []
        # time = -1
        # for i, t in enumerate(tasks):
        #     if len(minheap) == 0:
        #         heappush(minheap, (t[1], hm[(t[0], t[1])], t[0]))
        #         time = t[0]
        #     else:
        #         if t[0] == minheap[-1][2]:
        #             heappush(minheap, (t[1],hm[(t[0], t[1])], t[0]))
        #         else:
        #             break
        # # print(minheap)
        # idx = len(minheap)        
        # n = len(tasks)
        # ans = []
        # while n > 0:
        #     # print(minheap)
        #     p, i, s = heappop(minheap)
        #     time = time + p
        #     ans.append(i)
        #     for j in range(idx, len(tasks)):
        #         if tasks[j][0] <= time:
        #             heappush(minheap, (tasks[j][1], hm[(tasks[j][0], tasks[j][1])], tasks[j][0]))
        #             idx = j + 1
        #         else:
        #             idx = j
        #             break            
        #     n = n - 1

        # return ans       



