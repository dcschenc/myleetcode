class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Count the number of zeros in the original array.
        zeros = arr.count(0)
        
        # Calculate the final length of the modified array.
        n = len(arr)
        final_length = n + zeros
        
        # Start from the end of the original array and the final array.
        for i in range(n - 1, -1, -1):
            # If we're within the bounds of the final array, copy the element.
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            
            # If the element is zero, duplicate it and decrement the zeros count.
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0

