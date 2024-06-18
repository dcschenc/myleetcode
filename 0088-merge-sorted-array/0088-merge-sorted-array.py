class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        # if n == 0:
        #     return
        # i, j = 0, 0
        # res = []
        # while i < m and j < n:
        #     if nums1[i] > nums2[j]:
        #         res.append(nums2[j])
        #         j += 1
        #     else:
        #         res.append(nums1[i])
        #         i += 1
        # while i < m:
        #     res.append(nums1[i])
        #     i += 1
        # while j < n:
        #     res.append(nums2[j])
        #     j += 1
        # k = 0
        # while k < m + n:
        #     nums1[k] = res[k]
        #     k += 1
            

        # i, j = 0, 0
        # while i < m:
        #     if nums1[i] > nums2[0]:
        #         tmp = nums1[i]
        #         nums1[i] = nums2[0]              
                
        #         j = 1
        #         while j < n:
        #             if nums2[j] < tmp:
        #                 nums2[j-1] = nums2[j]
        #             else:                        
        #                 break
        #             j += 1
        #         nums2[j-1] = tmp
        #     i += 1
        #     # print(nums1, nums2)
        # j = 0
        # while j < n:
        #     nums1[m+j] = nums2[j]
        #     j += 1
                
            
                