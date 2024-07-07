class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:   
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1101.The%20Earliest%20Moment%20When%20Everyone%20Become%20Friends   
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        for t, x, y in sorted(logs):
            if find(x) == find(y):
                continue
            p[find(x)] = find(y)
            n -= 1
            if n == 1:
                return t
        return -1

        def find(x):           
            return root[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                for i in range(len(root)):
                    if root[i] == rootY:
                        root[i] = rootX           
        
        root = [i for i in range(n)]
        # rank = [1] * n
        logs.sort(key=lambda x: x[0])
        for t, x, y in logs:
            union(x, y)
            if len(set(root)) == 1:
                return t
        
        return -1