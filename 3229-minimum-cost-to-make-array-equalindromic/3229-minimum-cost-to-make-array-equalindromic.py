class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/solutions/4415318/very-simple-python-solution-with-an-explanation-beats-100/
        #cost of converting array to 'palind' 
        def cost(palind):
            return sum([abs(palind - num) for num in nums])        
        #check if 'num' is a valid palindrome
        def check_pal(num):
            return str(num) == str(num)[::-1]

        nums.sort()
        #calculate the median
        if len(nums) % 2 == 1:
            median = nums[len(nums) // 2]
        else:
            median = round((nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2)
        
        if check_pal(median):
            return cost(median)
        
        #get closest palindrome from left and right sides of the median
        #and return the one with minimum cost
        left, right = median - 1, median + 1

        while not check_pal(left):
            left -= 1

        while not check_pal(right):
            right += 1
        
        return min(cost(left), cost(right))
