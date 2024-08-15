class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2962.Count%20Subarrays%20Where%20Max%20Element%20Appears%20at%20Least%20K%20Times
        queue = deque()
        i, n, mx = 0, len(nums), max(nums)
        ans = 0
        while i < n:
            if nums[i] == mx:
                queue.append(i)
                if len(queue) > k:
                    queue.popleft()
            if len(queue) == k:
                ans += queue[0] + 1
            i += 1
        return ans

        mx = max(nums)
        n = len(nums)
        ans = cnt = j = 0
        for x in nums:
            while j < n and cnt < k:
                cnt += nums[j] == mx
                j += 1
            if cnt < k:
                break
            ans += n - j + 1
            cnt -= x == mx
        return ans
    