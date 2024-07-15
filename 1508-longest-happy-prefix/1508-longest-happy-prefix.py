class Solution:
    def longestPrefix(self, s: str) -> str:
        # for i in range(1, len(s)):
        #     if s[:-i] == s[i:]:
        #         return s[i:]
        # return ''        

        n = len(s)
        lps = [0] * n  # Longest Prefix Suffix array
        length = 0     # Length of the previous longest prefix suffix
        i = 1

        # Loop calculates lps[i] for i = 1 to n-1
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # This is tricky. Consider the example "AAACAAAA" and i = 7.
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        # The longest happy prefix which is also a suffix
        longest_happy_prefix_length = lps[-1]
        return s[:longest_happy_prefix_length]