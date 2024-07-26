class FindSumPairs:
    # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1865.Finding%20Pairs%20With%20a%20Certain%20Sum
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = Counter(nums1)
        self.nums2 = nums2        
        self.nums2_hm = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        cur = self.nums2[index]
        self.nums2_hm[cur] -= 1
        self.nums2[index] += val
        self.nums2_hm[cur + val] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for k, v in self.nums1.items():
            if tot - k in self.nums2_hm:
                ans += v * self.nums2_hm[tot - k]
        return ans
        
        # for num in self.nums2:
        #     if tot - num in self.nums1:
        #         ans += self.nums1[tot-num]
        # return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)