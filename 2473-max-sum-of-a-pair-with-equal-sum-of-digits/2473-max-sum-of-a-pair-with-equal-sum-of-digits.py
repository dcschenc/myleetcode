class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2342.Max%20Sum%20of%20a%20Pair%20With%20Equal%20Sum%20of%20Digits
        d = defaultdict(int)
        ans = -1
        for v in nums:
            x, y = 0, v
            while y:
                x += y % 10
                y //= 10
            if x in d:
                ans = max(ans, d[x] + v)
            d[x] = max(d[x], v)
        return ans
        
        hm, n, ans = defaultdict(list), len(nums), -1
        for i in range(n):
            cur = str(nums[i])
            k = sum([int(c) for c in cur])
            # k = 0
            # for c in cur:
                # k += int(c)
            hm[k].append(nums[i])

        for v in hm.values():
            if len(v) > 1:
                v.sort()
                ans = max(ans, v[-2] + v[-1])
            # for a, b in combinations(v, 2):
                # ans = max(ans, a + b)
        return ans
        