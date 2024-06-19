class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums: return []       
        left, right = nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] == right + 1:
                right = nums[i]
            else:
                if left == right:
                    res.append(str(left))
                else:                    
                    res.append(f'{left}->{right}')
                left = right = nums[i]
                
        if left == right:
            res.append(str(left))
        else:
            res.append(f'{left}->{right}')

        return res
