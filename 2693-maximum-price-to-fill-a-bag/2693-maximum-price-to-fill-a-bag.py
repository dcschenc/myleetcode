class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2548.Maximum%20Price%20to%20Fill%20a%20Bag
        ans = 0
        for p, w in sorted(items, key=lambda x: x[1] / x[0]):
            v = min(w, capacity)
            ans += v / w * p
            capacity -= v
        return -1 if capacity else ans

        # hm = {}
        # items.sort(key = lambda x: x[0]/x[1], reverse = True)
        # t_price, t_weight = 0, 0
        # for price, weight in items:
        #     if t_weight + weight <= capacity:
        #         t_price += price
        #         t_weight += weight
        #         if t_weight == capacity:
        #             return t_price
        #     else:
        #         ratio = (capacity - t_weight) / weight
        #         t_price += price * ratio
        #         return t_price
        # return -1
