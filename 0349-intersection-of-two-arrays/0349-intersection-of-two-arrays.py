class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        nums1.sort()
        nums2.sort()
        arr=set()
        i,j=0,0
        while(i<n1 and j<n2):
            if(nums1[i]==nums2[j]):
                arr.add(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return arr

        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.intersection(set2))

        # res = set()
        # if len(nums1) < len(nums2):            
        #     for val in nums1:
        #         if val not in res and val in nums2:
        #             res.add(val)
        # else:
        #     for val in nums2:
        #         if val not in res and val in nums1:
        #             res.add(val)
        # return res