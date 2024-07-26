class Solution:
    def minSwaps(self, s: str) -> int:
        # Calculate the number of swaps required
        def count_swaps(ch1, ch2):
            count = 0
            for i in range(len(s)):
                if i % 2 == 0:
                    if s[i] != ch1:
                        count += 1
                else:
                    if s[i] != ch2:
                        count += 1
            return count // 2

        # Count the number of zeros and ones
        zeros = s.count('0')
        ones = s.count('1')
        
        # Check if it is impossible to make the string alternating
        if abs(zeros - ones) > 1:
            return -1
        
        if zeros == ones:
            return min(count_swaps('0', '1'), count_swaps('1', '0'))
        elif zeros > ones:
            return count_swaps('0', '1')
        else:
            return count_swaps('1', '0')

     
