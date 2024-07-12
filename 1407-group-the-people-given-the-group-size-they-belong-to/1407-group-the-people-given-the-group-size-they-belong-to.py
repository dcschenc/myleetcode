class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1282.Group%20the%20People%20Given%20the%20Group%20Size%20They%20Belong%20To
        hm = defaultdict(list)
        for i, s in enumerate(groupSizes):
            hm[s].append(i)
        groups = []
        for s, p in hm.items():
            cur, total = 0, len(p)
            while total > 0:
                group = []
                for i in range(s):
                    group.append(p[cur])
                    cur += 1
                groups.append(group)
                total = total - s
        return groups
            