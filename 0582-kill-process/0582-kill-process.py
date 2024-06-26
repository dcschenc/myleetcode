class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def dfs(node):
            ans.append(node)
            for child in hm[node]:
                dfs(child)

        hm = defaultdict(list)
        for i, child in enumerate(pid):
            parent = ppid[i]
            hm[parent].append(child)
        ans = []
        dfs(kill)
        return ans