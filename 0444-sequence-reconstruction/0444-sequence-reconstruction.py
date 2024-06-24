class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0444.Sequence%20Reconstruction
        g = defaultdict(list)
        indeg = [0] * len(nums)
        for seq in sequences:
            for a, b in pairwise(seq):
                g[a - 1].append(b - 1)
                indeg[b - 1] += 1

        q = deque(i for i, v in enumerate(indeg) if v == 0)
        while q:
            if len(q) > 1: return False
            i = q.popleft()
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return True
        
        # values = {x for seq in sequences for x in seq}
        # graph = {x: [] for x in values}
        # indegrees = {x: 0 for x in values}
        # for seq in sequences:
        #     for i in range(len(seq) - 1):
        #         s = seq[i]
        #         t = seq[i+1]
        #         graph[s].append(t)
        #         indegrees[t] += 1
        # queue = collections.deque()
        # for node, count in indegrees.items():
        #     if count == 0:
        #         queue.append(node)
        # res = []
        # while queue:
        #     if len(queue) != 1:
        #         return False
        #     source = queue.popleft()
        #     res.append(source)
        #     for target in graph[source]:
        #         indegrees[target] -= 1
        #         if indegrees[target] == 0:
        #             queue.append(target)
        # return len(res) == len(values) and res == nums