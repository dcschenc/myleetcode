class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum_xor = 0  # Initialize the maximum XOR value.
        mask = 0  # Initialize the mask, which is used to consider bits from the most significant bit down.
      
        # Start from the highest bit and go down to the least significant bit (31st to 0th bit).
        for i in range(31, -1, -1):
            mask = mask | (1 << i)  # Update the mask to include the next bit.
            prefixes = set()  # Create a set to store prefixes of the current length.
          
            # Collect all prefixes with bits up to the current bit.
            for num in nums:
                prefixes.add(num & mask)  # Bitwise AND to isolate the prefix.
          
            # We assume the new bit is '1' and combine it with maximum XOR so far.
            proposed_max = maximum_xor | (1 << i)
          
            # Check if there's a pair of prefixes which XOR equals our proposed maximum so far.
            for prefix in prefixes:
                if (prefix ^ proposed_max) in prefixes:
                    maximum_xor = proposed_max  # Update the maximum XOR since we found a pair.
                    break  # No need to check other prefixes.
                  
        # After checking all bits, return the maximum XOR we found.
        return maximum_xor

class Trie:
    def __init__(self):
        self.root = {}
        self.m = 0
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        
    def compare(self, word, i):
        node = self.root
        t = ""
        a, b = '0', '1'
        for ch in word:
            if ch == a and b in node:
                t += b
                node = node[b]
            elif ch == b and a in node:
                t += a
                node = node[a]
            else:
                t += ch
                node = node[ch]
        self.m = max(self.m, int(t, 2)^i)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie=Trie()
        for i in nums:
            word = "{:032b}".format(i)
            trie.insert(word)
        for i in nums:
            word="{:032b}".format(i)
            trie.compare(word, i)
        return trie.m