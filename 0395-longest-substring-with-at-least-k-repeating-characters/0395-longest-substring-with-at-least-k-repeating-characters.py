from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_length = 0
        n = len(set(s))

        for n_unique_chars in range(1, n + 1):
            left = 0
            char_counts = {}
            at_least_k = 0

            for right in range(len(s)):
                char_counts[s[right]] = char_counts.get(s[right], 0) + 1

                if char_counts[s[right]] == k:
                    at_least_k += 1

                while len(char_counts) > n_unique_chars:
                    char_counts[s[left]] -= 1
                    if char_counts[s[left]] == k - 1:
                        at_least_k -= 1
                    if char_counts[s[left]] == 0:
                        del char_counts[s[left]]
                    left += 1

                if at_least_k == n_unique_chars:
                    max_length = max(max_length, right - left + 1)

        return max_length