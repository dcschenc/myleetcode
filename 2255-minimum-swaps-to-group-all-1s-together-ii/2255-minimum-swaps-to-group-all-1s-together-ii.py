class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2134.Minimum%20Swaps%20to%20Group%20All%201's%20Together%20II
        k = nums.count(1)
        mx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k, n + k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n) % n]
            mx = max(mx, cnt)
        return k - mx

        # def get_min(cnt, d):
        #     nonlocal ans
        #     counter = Counter(nums[:cnt])
        #     for i in range(cnt, n):
        #         ans = min(ans, abs(cnt - counter[d]))            
        #         counter[nums[i]] += 1
        #         counter[nums[i-cnt]] -= 1
        #     ans = min(ans, abs(cnt - counter[d]))  

        # ones, zeros = nums.count(1), nums.count(0)
        # n, ans = len(nums), float('inf')
        # get_min(ones, 1)
        # get_min(zeros, 0)

        # return ans