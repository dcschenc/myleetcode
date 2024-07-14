class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        # hm = defaultdict(list)
        # for rid, r, v, p, d in restaurants:
        #     hm[v].append((p, d, r, rid))
        ans = []
        for rid, r, v, p, d in restaurants:
            if veganFriendly and v == 0:
                continue
            if p <= maxPrice and d <= maxDistance:                
                ans.append((r, rid))
        ans.sort(reverse=True)
        return [rid for r, rid in ans]