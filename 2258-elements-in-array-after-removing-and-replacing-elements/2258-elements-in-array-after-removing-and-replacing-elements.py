class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ans = []
        for t, idx in queries:
            times = t // n
            if times % 2 == 0:
                mod = t % n
                left = n - mod
                if idx >= left:
                    ans.append(-1)
                else:
                    ans.append(nums[mod + idx])
            else:
                left = t % n
                if idx >= left:
                    ans.append(-1)
                else:
                    ans.append(nums[idx])            
        return ans

        