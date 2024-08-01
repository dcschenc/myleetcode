class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_1 = set(nums1)
        set_2 = set(nums2)
        answer = [[],[]]
        for v in set_1:
            if v not in set_2:
                answer[0].append(v)
        for v in set_2:
            if v not in set_1:
                answer[1].append(v)
        return answer
