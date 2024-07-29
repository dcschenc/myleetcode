class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1, set2, set3 = set(nums1), set(nums2), set(nums3)
        s = set1 | set2 | set3
        ans = []
        for num in s:
            cnt = 0
            if num in set1:
                cnt += 1
            if num in set2:
                cnt += 1
            if num in set3:
                cnt += 1
            if cnt >= 2:
                ans.append(num)
        return ans