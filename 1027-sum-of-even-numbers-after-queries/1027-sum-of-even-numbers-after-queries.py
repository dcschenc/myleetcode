class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # simulation
        ans = []
        total = sum(v for v in nums if v % 2 == 0)
        for val, idx in queries:
            cur = nums[idx]
            nums[idx] += val
            if cur % 2 == 0:
                if val % 2 == 0:
                    total = total + val
                else:
                    total = total - cur
            else:
                if val % 2 != 0:
                    total = total + nums[idx]
            ans.append(total)
        return ans