class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = Counter(x for x in nums if x % 2 == 0)
        ans, mx = -1, 0
        for x, v in cnt.items():
            if v > mx or (v == mx and ans > x):
                ans, mx = x, v
        return ans
        
        # hm = defaultdict(int)
        # for num in nums:
        #     if num%2 == 0:
        #         hm[num] += 1
        # sorted_items = sorted(hm.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        # return sorted_items[0][0] if sorted_items else -1