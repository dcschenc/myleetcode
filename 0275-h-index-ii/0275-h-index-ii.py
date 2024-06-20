class Solution:
    def hIndex(self, citations: List[int]) -> int:   
        #######  [0,1,3,5,6] #########
        # n = len(citations)
        # left, right = 0, n - 1

        # while left <= right:
        #     mid = left + (right - left) // 2
        #     h = n - mid  # Calculate the h-index using the formula

        #     if citations[mid] == h:
        #         return h  # Found the h-index
        #     elif citations[mid] < h:
        #         left = mid + 1  # Move the left pointer to the right
        #     else:
        #         right = mid - 1  # Move the right pointer to the left

        # return n - left  # Return the h-index
        
        citations.sort(reverse=True)
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right)//2
            # if mid  == citations[mid]:
            #     return mid 
            if mid  < citations[mid]:
                left = mid + 1                
            else:    
                right = mid - 1
        return left