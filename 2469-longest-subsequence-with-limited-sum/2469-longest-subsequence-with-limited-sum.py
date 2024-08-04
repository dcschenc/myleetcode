class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2389.Longest%20Subsequence%20With%20Limited%20Sum
        # nums.sort()
        # s = list(accumulate(nums))
        # return [bisect_right(s, q) for q in queries]

        nums.sort()
        ans, n = [], len(nums)
        for q in queries:
            cur, i = 0, 0
            while i < n and cur + nums[i] <= q:
                cur += nums[i]
                i += 1
            ans.append(i)
        return ans
                
            
                
            