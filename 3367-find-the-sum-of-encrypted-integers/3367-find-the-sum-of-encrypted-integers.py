class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            num = str(num)
            total += int(len(num) * max(num))
        return total
        
