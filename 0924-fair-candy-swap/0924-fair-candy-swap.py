class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        swap = False
        if sum(aliceSizes) > sum(bobSizes):
            aliceSizes, bobSizes = bobSizes, aliceSizes
            swap = True
        total = (sum(aliceSizes) + sum(bobSizes))/2
        target = total - sum(aliceSizes)
        bset = set(bobSizes)
        res = [-1, -1]
        for i in range(len(aliceSizes)):
            if aliceSizes[i] + target in bset:
                res[0] = aliceSizes[i]
                res[1] = aliceSizes[i] + target
                
        # aliceSizes.sort()
        # bobSizes.sort()
        # L, R = 0, 0
        # res = [-1, -1]
        # while True:
        #     # print(aliceSizes, bobSizes, L, R)
        #     if bobSizes[R] - aliceSizes[L] == target:
        #         res[0] = aliceSizes[L]
        #         res[1] = bobSizes[R]
        #         break
        #     elif bobSizes[R] - aliceSizes[L] < target:
        #         R = R + 1
        #     else:
        #         L = L + 1
        
        return reversed(res) if swap else res