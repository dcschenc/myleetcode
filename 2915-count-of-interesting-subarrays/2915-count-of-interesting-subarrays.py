class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2845.Count%20of%20Interesting%20Subarrays
        arr = [int(x % modulo == k) for x in nums]
        cnt = Counter()
        cnt[0] = 1
        ans = s = 0
        for x in arr:
            s += x
            ans += cnt[(s - k) % modulo]
            cnt[s % modulo] += 1
        return ans


        # n, ans = len(nums), 0
        # pre = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     pre[i] = pre[i-1]
        #     if nums[i-1] % modulo == k:
        #         pre[i] += 1

        # hm = defaultdict(int)
        # hm[0] = 1
        # for i in range(1, n + 1):
        #     cur_mod = pre[i] % modulo
        #     t = (cur_mod - k) % modulo
        #     if t in hm:            
        #         ans += hm[t]
        #     hm[cur_mod] += 1
        # return ans
            