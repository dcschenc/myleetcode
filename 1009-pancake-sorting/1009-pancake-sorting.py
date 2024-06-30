class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # Helper function to reverse the array from start to index 'k'.
        def flip(k):
            start = 0
            while start < k:                
                arr[start], arr[k] = arr[k], arr[start]
                start += 1
                k -= 1

        n = len(arr)
        flips = []  # To store the sequence of flips

        # Start sorting from the end of the array
        for target_index in range(n - 1, 0, -1):
            # Find the index of the next largest element to sort
            max_index = arr.index(target_index + 1)
          
            # If the largest element is not already in place
            if max_index != target_index:
                # Bring the largest element to the start if it's not already there
                if max_index > 0:
                    flips.append(max_index + 1)
                    flip(max_index)
                # Now flip the largest element to its correct target index
                flips.append(target_index + 1)
                flip(target_index)

        return flips
