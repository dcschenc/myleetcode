class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nums[i] = num        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx, val in self.nums.items():
            if idx in vec.nums:
                ans += val * vec.nums[idx]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)