class Solution:
    def minJumps(self, arr: List[int]) -> int:
        hm = defaultdict(list)
        n = len(arr)
        for i in range(n):
            hm[arr[i]].append(i)
        queue = deque()
        queue.append(0)
        steps, visited = 0, set()
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n - 1:
                    return steps
                if cur in visited:
                    continue
                visited.add(cur)
                if cur - 1 >= 0:
                    queue.append(cur - 1)
                if cur + 1 < n:
                    queue.append(cur + 1)
                for j in hm[arr[cur]]:
                    if j not in visited:
                        queue.append(j)
                hm[arr[cur]].clear() # this is very import to avoid redundant earch, otherwise memoney not enough
            steps += 1
        