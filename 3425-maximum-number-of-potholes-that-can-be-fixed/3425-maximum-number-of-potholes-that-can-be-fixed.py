class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        n = len(road)
        i = ans = 0
        x_arr = road.split('.')
        x_arr = [len(x) for x in x_arr if len(x) != 0]
        x_arr.sort(reverse=True)
        for x in x_arr:
            if x + 1 < budget:
                ans += x
                budget -= x + 1
            else:
                ans += budget - 1
                break
        return ans

        