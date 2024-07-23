class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1702.Maximum%20Binary%20String%20After%20Change
        k = binary.find('0')
        if k == -1:
            return binary
        k += binary[k + 1 :].count('0')
        return '1' * k + '0' + '1' * (len(binary) - k - 1)
        
        # Find the index of the first '0' in the binary string
        first_zero_index = binary.find('0')
      
        # If there's no '0', the binary string is already at its maximum value
        if first_zero_index == -1:
            return binary
      
        # Calculate the position for the '0' after conversion to maximum binary string
        # It counts the number of '0's after the first '0' found, and adds this to the index of the first '0'
        zero_position_after_conversion = first_zero_index + binary[first_zero_index + 1:].count('0')
      
        # Construct the maximum binary string:
        # 1. A string of '1's with length equal to the position of '0' after conversion
        # 2. Followed by a single '0'
        # 3. And the rest of the string filled with '1's
        # Total length stays the same as the original string
        maximum_binary = '1' * zero_position_after_conversion + '0' + '1' * (len(binary) - zero_position_after_conversion - 1)
      
        return maximum_binary