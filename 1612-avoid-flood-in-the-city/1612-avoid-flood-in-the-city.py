from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1488.Avoid%20Flood%20in%20The%20City       
        lake_map = {}
        dry_days = []
        result = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                result[i] = 1  # To be determined later
            else:
                if lake in lake_map:
                    last_rain = lake_map[lake]
                    pos = bisect_left(dry_days, last_rain)
                    if pos == len(dry_days):
                        return []
                    dry_day = dry_days.pop(pos)
                    result[dry_day] = lake
                lake_map[lake] = i
                result[i] = -1
        
        return result

        # n = len(rains)
        # ans = [-1] * n
        # sunny = SortedList()
        # rainy = {}
        # for i, v in enumerate(rains):
        #     if v:
        #         if v in rainy:
        #             idx = sunny.bisect_right(rainy[v])
        #             if idx == len(sunny):
        #                 return []
        #             ans[sunny[idx]] = v
        #             sunny.discard(sunny[idx])
        #         rainy[v] = i
        #     else:
        #         sunny.add(i)
        #         ans[i] = 1
        # return ans