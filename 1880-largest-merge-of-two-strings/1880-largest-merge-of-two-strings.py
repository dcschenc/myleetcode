class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1754.Largest%20Merge%20Of%20Two%20Strings
        i = j = 0
        ans = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        ans.append(word1[i:])
        ans.append(word2[j:])
        return "".join(ans)
        
        # n, m = len(word1), len(word2)
        # i, j = 0, 0
        # ans = ''
        # while i < n and j < m:
        #     if word1[i] > word2[j]:
        #         ans += word1[i]
        #         i += 1
        #     elif word1[i] < word2[j]:
        #         ans += word2[j]
        #         j += 1
        #     else:
        #         ans += word1[i]
        #         if i + 1 < n and j + 1 < m:
        #             if word1[i+1:] >= word2[j+1:]:
        #                 i += 1
        #             else:
        #                 j += 1
        #         elif i + 1 < n:
        #             i += 1
        #         else:
        #             j += 1
        # if i < n:
        #     ans += word1[i:]
        # if j < m:
        #     ans += word2[j:]
        # return ans

        