class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(node, parent):             
            total = 1
            for c in children[node]:
                if c != parent:
                    child = dfs(c, node)
                    ans[0] += math.ceil(child / seats)
                    total += child            
            return total
        
        children = defaultdict(list)
        for p, c in roads:
            children[p].append(c)
            children[c].append(p)
        ans = [0]
        dfs(0, -1)
        return ans[0]
        