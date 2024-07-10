from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:  
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1202.Smallest%20String%20With%20Swaps             
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY] < rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY] = rootX
                    rank[rootX] += 1

        root = [i for i in range(len(s))]
        rank = [0] * len(s)
        for x, y in pairs:
            union(x, y)
        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(s[i])
        for group in groups.values():
            group.sort(reverse=True)
        # print(groups.values())
        result = []
        for i in range(len(s)):
            group_id = find(i)
            result.append(groups[group_id].pop())
        return ''.join(result)

