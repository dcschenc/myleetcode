class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2832.Maximal%20Range%20That%20Each%20Element%20Is%20Maximum%20in%20It
        n = len(nums)
        ans = [0] * n
        stack = [(float(inf), -1)]
        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()            
            ans[i] = i - stack[-1][1]
            stack.append((nums[i], i))

        stack = [(float(inf), n)]
        for i in range(n - 1, -1, -1):
            while stack and stack[-1][0] < nums[i]:
                stack.pop()
            ans[i] += stack[-1][1] - i - 1
            stack.append((nums[i], i))
        
        return ans
