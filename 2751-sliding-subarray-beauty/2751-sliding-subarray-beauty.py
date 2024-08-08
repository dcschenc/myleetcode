from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2653.Sliding%20Subarray%20Beauty
        def f(x: int) -> int:
            s = 0
            for i in range(50):
                s += cnt[i]
                if s >= x:
                    return i - 50
            return 0

        cnt = [0] * 101
        for v in nums[:k]:
            cnt[v + 50] += 1
        ans = [f(x)]
        for i in range(k, len(nums)):
            cnt[nums[i] + 50] += 1
            cnt[nums[i - k] + 50] -= 1
            ans.append(f(x))
        return ans

       
        # sl = SortedList()
        # ans = []
        # for i, num in enumerate(nums):
        #     sl.add(num)
        #     if i >= k:
        #         sl.remove(nums[i-k])
        #     if i >= k - 1:
        #         if sl[x-1] < 0:
        #             ans.append(sl[x-1])
        #         else:
        #             ans.append(0)
        # return ans
            
        