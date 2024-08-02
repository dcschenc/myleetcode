from heapq import heappush, heappop, heapify
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2233.Maximum%20Product%20After%20K%20Increments
        # heapify(nums)
        # for _ in range(k):
        #     heappush(nums, heappop(nums) + 1)
        # ans = 1
        # mod = 10**9 + 7
        # for v in nums:
        #     ans = (ans * v) % mod
        # return ans

        n = len(nums)
        mod = 10**9 + 7
        heapify(nums)
        while k > 0:                        
            min_val = heappop(nums)            
            heappush(nums, min_val + 1)
            k -= 1
        product = 1
        for num in nums:
            product = (product * num) % mod
        return product
