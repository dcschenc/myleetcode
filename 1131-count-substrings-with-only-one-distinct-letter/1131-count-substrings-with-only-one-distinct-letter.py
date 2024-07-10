from collections import defaultdict
class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        total = left = 0
        for right in range(n + 1):
            if right == n or s[left] != s[right]:
                len_substring = right - left
                # more details about the sum of the arithmetic sequence:
                # https://en.wikipedia.org/wiki/Arithmetic_progression#Sum
                total += (1 + len_substring) * len_substring // 2
                left = right
        return total

        # total = 1
        # count = 1
        # for i in range(1, len(s)):
        #     if s[i] == s[i-1]:
        #         count += 1
        #     else:
        #         count = 1
        #     total += count
        # return total

        # hm = defaultdict(int)
        # for i in range(len(s)):
        #     cur = s[i]
        #     hm[cur] += 1
        #     for j in range(i+1, len(s)):
        #         if s[j] != s[i]:
        #             break
        #         cur += s[j]
        #         hm[cur] += 1
        # # print(hm)
        # return sum(hm.values())