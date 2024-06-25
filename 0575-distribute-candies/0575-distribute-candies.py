class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        n = n//2
        candyType = set(candyType)
        if len(candyType) <= n:
            return len(candyType)
        else:
            return n
            
        # for i, t in enumerate(candyType):
        #     if t not in types:
        #         types.add(t)
        #         n -= 1
        #         if n == 0:
        #             break
        # return len(types)