class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1300.Sum%20of%20Mutated%20Array%20Closest%20to%20Target
        # n = len(arr)
        # arr.sort()
        # cur, ans = 0, inf
        # presum = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     presum[i] = presum[i-1] + arr[i-1]
        # diff = inf
        # for val in range(max(arr) + 1):
        #     idx = bisect_right(arr, val)
        #     cur_diff = abs((n - idx) * val + presum[idx] - target)
        #     if cur_diff < diff:
        #         diff = cur_diff
        #         ans = val                       
        # return ans
        
        arr.sort()
        s = list(accumulate(arr, initial=0))
        ans, diff = 0, inf
        for value in range(max(arr) + 1):
            i = bisect_right(arr, value)
            d = abs(s[i] + (len(arr) - i) * value - target)
            if diff > d:
                diff = d
                ans = value
        return ans