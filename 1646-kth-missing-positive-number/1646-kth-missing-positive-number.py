class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:       
        missing_count = 0
        previous_number = 0

        for num in arr:
            current_missing = num - previous_number - 1
            if missing_count + current_missing >= k:
                return previous_number + (k - missing_count)
            missing_count += current_missing
            previous_number = num

        # If k-th missing number is beyond the last element in the array
        return arr[-1] + (k - missing_count)


        # https://algo.monster/liteproblems/1539
        # If the first element is larger than k, the k-th positive missing number would be k
        if arr[0] > k:
            return k
      
        # Use binary search to find k-th positive missing number
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2  # Use integer division for Python 3
          
            # Calculate the number of negative elements up to index mid
            missing_until_mid = arr[mid] - mid - 1
          
            # If the number of missing elements is greater or equals k, look in the left half
            if missing_until_mid >= k:
                right = mid
            else:
                left = mid + 1  # Otherwise, look in the right half

        # After binary search, calculate the k-th missing positive number
        # by adding k to the number at the index `left - 1` in the array 
        # and then adjust it by subtracting the missing count until that point
        missing_until_left_minus_one = arr[left - 1] - (left - 1) - 1
        kth_missing_positive = arr[left - 1] + k - missing_until_left_minus_one
        return kth_missing_positive
        
         
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k


        i = 1
        hm = set(arr)
        while True:        
            if i not in hm:
                k -= 1
                if k == 0:
                    return i
            i += 1
