class Solution:
    def check(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1752.Check%20if%20Array%20Is%20Sorted%20and%20Rotated
        n = len(nums)
        count_breaks = 0
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count_breaks += 1
        
        return count_breaks <= 1

        return sum(nums[i - 1] > v for i, v in enumerate(nums)) <= 1
        
        n = len(nums)
        for i in range(n):
            start = i
            flag = True
            for j in range(1, n):
                if nums[(start + j) % n] < nums[(start + j  - 1) % n]:
                    flag = False
                    break
            if flag:
                return True
        return False
