class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2958.Length%20of%20Longest%20Subarray%20With%20at%20Most%20K%20Frequency
        cnt = defaultdict(int)
        ans = j = 0
        for i, x in enumerate(nums):
            cnt[x] += 1
            while cnt[x] > k:
                cnt[nums[j]] -= 1
                j += 1
            ans = max(ans, i - j + 1)
        return ans

        # n, ans = len(nums), 0
        # start, hm = 0, defaultdict(deque)
        # for i in range(n):
        #     cur = nums[i]
        #     queue = hm[cur]
        #     queue.append(i)
        #     if len(queue) > k:
        #         j = queue.popleft()
        #         if j + 1 > start:
        #             start = j + 1            
        #     ans = max(ans, i - start + 1)
                
        # return ans

        