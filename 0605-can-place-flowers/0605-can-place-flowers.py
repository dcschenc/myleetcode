class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # n = len(flowerbed)
        # if n == 0:
        #     return True
        # length = len(flowerbed)
        # for i, v in enumerate(flowerbed):
        #     res = False
        #     if v == 0:
        #         if i== 0 and (i+1 < length and flowerbed[i+1] == 0 or length==1):
        #             res = True
        #         elif 0 < i < length-2  and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
        #             res = True
        #         elif i == length-1 and flowerbed[i-1] == 0:
        #             res = True
        #         if res:
        #             n -= 1
        #             flowerbed[i] = 1
        #     if n == 0:
        #         break
        # return n == 0
                
        ######## sliding window #############        
        count = 0
        flowerbed = [0] + flowerbed + [0]  # Add 0s at the beginning and end to handle boundaries.
        
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        
        return count >= n