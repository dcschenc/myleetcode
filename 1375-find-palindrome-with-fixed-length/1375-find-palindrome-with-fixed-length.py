class Solution:
    def kthPalindrome(self, queries: List[int], int_length: int) -> List[int]:
        # Calculate the number of digits in the first half of the palindrome
        half_length = (int_length + 1) >> 1
      
        # Define the start and end of the range for the first half of the palindrome
        start = 10 ** (half_length - 1)
        end = (10 ** half_length) - 1
      
        # Initialize an empty list to store the answers
        answers = []
      
        # Iterate over each query to find the k-th palindrome
        for query in queries:
            # Calculate the value in the first half by offsetting the start with the query index
            value = start + query - 1
          
            # If the value exceeds the end boundary, the palindrome doesn't exist
            if value > end:
                answers.append(-1)
                continue
          
            # Convert the first half to a string
            half_str = str(value)
          
            # Construct the full palindrome by concatenating the first half and its reverse
            # If the integer length is odd, skip the last digit of the reversed half
            palindrome = half_str + half_str[::-1][int_length % 2:]
          
            # Append the palindrome to the answers list, converting it back to an integer
            answers.append(int(palindrome))
      
        # Return the list of answers
        return answers
