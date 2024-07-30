class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append((num, i))        
        arr.sort(key=lambda x: x[0], reverse=True)
        ans = arr[:k]
        ans.sort(key=lambda x: x[1])
        return [v for v, i in ans]
        