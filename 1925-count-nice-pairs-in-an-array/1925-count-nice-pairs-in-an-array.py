from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1814.Count%20Nice%20Pairs%20in%20an%20Array
        n = len(nums)
        total = n * (n - 1)//2
        counter = defaultdict(int)
        for i, num in enumerate(nums):
            key = num - int(str(num)[::-1])
            counter[key] += 1
        cnt = 0
        for k, v in counter.items():
            cnt += v * (v - 1)//2
        return cnt % (10 ** 9 + 7)