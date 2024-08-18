class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans = 0
        seen = set()
        for num in nums:
            if num in seen:
                ans ^= num
            seen.add(num)
        return ans