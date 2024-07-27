class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1915.Number%20of%20Wonderful%20Substrings        
        count = defaultdict(int)
        count[0] = 1  # Start with the initial mask
        current_mask = 0
        wonderful_count = 0
        
        for char in word:
            # Flip the bit corresponding to the current character
            current_mask ^= (1 << (ord(char) - ord('a')))
            
            # Count substrings ending at this position with the current_mask
            wonderful_count += count[current_mask]
            
            # Check for masks differing by exactly one bit
            for i in range(10):
                test_mask = current_mask ^ (1 << i)
                wonderful_count += count[test_mask]
            
            # Update the count of the current mask
            count[current_mask] += 1
        
        return wonderful_count
        
        # Create the frequency map
        # Key = bitmask, Value = frequency of bitmask key
        freq = {}

        # The empty prefix can be the smaller prefix, which is handled like this
        freq[0] = 1

        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - 97

            # Flip the parity of the c-th bit in the running prefix mask
            mask ^= (1 << bit)

            # Count smaller prefixes that create substrings with no odd occurring letters
            if mask in freq:
                res += freq[mask]
                freq[mask] += 1
            else:
                freq[mask] = 1

            # Loop through every possible letter that can appear an odd number of times in a substring
            for odd_c in range(0, 10):
                if (mask ^ (1 << odd_c)) in freq:
                    res += freq[mask ^ (1 << odd_c)]

        return res