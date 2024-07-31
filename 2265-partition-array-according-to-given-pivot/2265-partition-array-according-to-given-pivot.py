class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []
        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
        ans = left
        ans.extend([pivot] * (len(nums) - len(left) - len(right)))
        ans.extend(right)
        return ans