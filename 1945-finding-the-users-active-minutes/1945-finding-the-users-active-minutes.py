class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1817.Finding%20the%20Users%20Active%20Minutes
        hm = defaultdict(set)
        for u, t in logs:
            hm[u].add(t)
        uam = defaultdict(int)
        for u, v in hm.items():
            uam[len(v)] += 1        
        ans = []
        for i in range(k):
            ans.append(uam[i + 1])
        return ans