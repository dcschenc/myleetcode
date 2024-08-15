class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        # Convert lists into sets for efficient set operations
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
      
        # Get the length of the first list
        list_length = len(nums1)
      
        # Calculate unique elements in nums1 not in nums2
        # Limit the count to half of nums1's length because we aim for balanced numbers
        unique_nums1 = min(len(set_nums1 - set_nums2), list_length // 2)
      
        # Calculate unique elements in nums2 not in nums1
        # Limit the count to half of nums1's length for the same reason as above
        unique_nums2 = min(len(set_nums2 - set_nums1), list_length // 2)
      
        # Count elements common to both sets
        common_elements = len(set_nums1 & set_nums2)
      
        # Maximize set size by combining the unique and common elements
        # Ensure the combined size does not exceed the length of nums1
        max_set_size = min(unique_nums1 + unique_nums2 + common_elements, list_length)
      
        return max_set_size
