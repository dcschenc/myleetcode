class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:      
        x, y = x - 1, y - 1
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                a = j - i
                b = abs(i - x) + 1 + abs(j - y)
                c = abs(i - y) + 1 + abs(j - x)
                ans[min(a, b, c) - 1] += 2
        return ans
        
        hm = defaultdict(int)
        for i in range(1, n+1):
            queue = deque()
            queue.append(i)            
            visited = set()
            k = 0
            while queue:
                for _ in range(len(queue)):
                    cur = queue.popleft()
                    if cur in visited:
                        continue
                    visited.add(cur)
                    if k > 0:
                        hm[k] += 1
                    if cur + 1 <= n:
                        queue.append(cur + 1)
                    if cur - 1 >= 1:
                        queue.append(cur - 1)
                    if cur == x:
                        queue.append(y)
                    if cur == y:
                        queue.append(x)
                k += 1
        ans = []
        for _, v in sorted(hm.items(), key=lambda x: x[0]):
            ans.append(v)
        while len(ans) < n:
            ans.append(0)
        return ans