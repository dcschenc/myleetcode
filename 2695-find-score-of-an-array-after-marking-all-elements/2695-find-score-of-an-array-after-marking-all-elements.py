class Solution:
    def findScore(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2593.Find%20Score%20of%20an%20Array%20After%20Marking%20All%20Elements
        heaps, n = [], len(nums)
        seen = [False] * n
        for i, num in enumerate(nums):
            heappush(heaps, (num, i))
        total = 0
        while heaps:
            num, i = heappop(heaps)           
            if seen[i] == False:
                total += num
                seen[i] = True
                if i - 1 >= 0:
                    seen[i - 1] = True
                if i + 1 < n:
                    seen[i + 1] = True
        return total