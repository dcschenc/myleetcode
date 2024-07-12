from collections import defaultdict
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent_hm = {}
        for region in regions:
            parent = region[0]
            for child in region[1:]:
                parent_hm[child] = parent
                
        ancestors = set()
        while region1 in parent_hm:
            ancestors.add(region1)
            region1 = parent_hm[region1]
        while region2 in parent_hm:
            if region2 in ancestors:
                return region2
            region2 = parent_hm[region2]
        return region1
        

        # # running = 0
        # n = regions
        # hm = {}
        # graph = defaultdict(set)
        # for region in regions:
        #     u = region[0]
        #     # if u not in hm:
        #     #     hm[u] = running
        #     #     running += 1
        #     for v in region[1:]:
        #         # if v not in hm:
        #         #     hm[v] = running
        #         #     running += 1
        #             graph[u].add(v)
        # # print(graph)


        