class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both the arrays first...
        # nums1.sort()
        # nums2.sort()
        # # Use two pointers i and j for the two arrays and initialize both with zero.
        # i = 0
        # j = 0
        # # Create a output list to store the output...
        # output = []
        # while i < len(nums1) and j < len(nums2):            
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums2[j] < nums1[i]:
        #         j += 1     
        #     else:
        #         output.append(nums1[i])
        #         i += 1
        #         j += 1
        # return output 

        # Create a dictionary to count the occurrences of elements in nums1.
        count_dict = {}
        result = []

        # Populate the dictionary with counts from nums1.
        for num in nums1:
            count_dict[num] = count_dict.get(num, 0) + 1

        # Check nums2 for common elements and decrement the counts.
        for num in nums2:
            if num in count_dict and count_dict[num] > 0:
                result.append(num)
                count_dict[num] -= 1

        return result

        # dictionary approach
        # dict_1 = {}
        # for val in nums1:
        #     if val in dict_1:
        #         dict_1[val].append(val)
        #     else:
        #         dict_1[val] = [val]
                
        # dict_2 = {}
        # for val in nums2:
        #     if val in dict_2:
        #         dict_2[val].append(val)
        #     else:
        #         dict_2[val] = [val]
        # res = []
        # for i in range(1001):
        #     if i in dict_1 and i in dict_2:
        #         if len(dict_1[i]) <= len(dict_2[i]):
        #             res.extend(dict_1[i])
        #         else:
        #             res.extend(dict_2[i])
        # return res
        
        