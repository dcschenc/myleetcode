class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(r):
            m, n = len(houses), len(heaters)
            i = j = 0
            while i < m:
                if j >= n:
                    return False
                mi = heaters[j] - r
                mx = heaters[j] + r
                if houses[i] < mi:
                    return False
                if houses[i] > mx:
                    j += 1
                else:
                    i += 1
            return True
            
        houses.sort()
        heaters.sort()
        left, right = 0, int(1e9)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

        # houses.sort()
        # heaters.sort()
        # res = [-1] * len(houses)
        # i, j = 0, 0
        # while i < len(houses):
        #     if houses[i] == heaters[j]:
        #         res[i] = 0
        #         i += 1
        #     elif houses[i] < heaters[j]:
        #         res[i] = heaters[j] - houses[i]
        #         i += 1
        #     else:
        #         while j + 1 < len(heaters) and houses[i] > heaters[j+1]:
        #             j += 1
        #         if j + 1< len(heaters):
        #             res[i] = min(houses[i] - heaters[j], heaters[j+1] - houses[i])
        #         else:
        #             res[i] = houses[i] - heaters[j]
        #         i += 1
        # return max(res)

        # for i in range(len(houses)):
        #     found = False
        #     for j in range(len(heaters)):
        #         if heaters[j] >= houses[i]:
        #             res[i] = heaters[j] - houses[i]
        #             if j > 0:
        #                 res[i] = min(res[i], houses[i] - heaters[j-1])
        #             found = True
        #             break
        #     if found == False:
        #         res[i] = houses[i] - heaters[len(heaters)-1]
        # # print(res)
        # return max(res)
        