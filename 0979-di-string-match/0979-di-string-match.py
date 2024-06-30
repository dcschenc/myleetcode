class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lo, hi = 0, len(s)
        ans = []
        for x in s:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]


        # Understanding the Pattern:

# The given pattern consists of "I" (increase) and "D" (decrease).
# For each "I," we want the next number to be greater.
# For each "D," we want the next number to be smaller.
# Creating the Permutation:

# We start with the smallest and largest numbers (0 and N, where N is the length of the pattern).
# We iterate through the pattern and decide whether to use the current smallest or largest number based on whether the next operation is "I" or "D."
# We increment or decrement the pointer accordingly.