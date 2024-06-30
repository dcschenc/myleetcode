from collections import defaultdict
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        for x in sorted(arr, key = abs):
            if count[x] == 0: 
                continue
            if count[2*x] == 0: 
                return False
            count[x] -= 1
            count[2*x] -= 1

        return True

        # hm = defaultdict(int)
        # for i, num in enumerate(arr):
        #     hm[num] += 1
        
        # for k1 in sorted(hm.keys()):
        #     v1 = hm[k1]           
        #     if k1 == 0:
        #         hm[k1] = v1%2
        #         continue
        #     if k1 > 0:
        #         if k1*2 in hm:
        #             v2 = hm[k1*2]
        #             if  v1 > v2:
        #                 return False
        #             else:
        #                 hm[k1] = 0
        #                 hm[k1*2] -= v1
        #     else:
        #         if k1/2 in hm:
        #             v2 = hm[k1/2]
        #             if v1 > v2:
        #                 return False
        #             else:
        #                 hm[k1] = 0
        #                 hm[k1/2] -=  v1
        # for k, v in hm.items():
        #     if v != 0:
        #         return False
        # return True

