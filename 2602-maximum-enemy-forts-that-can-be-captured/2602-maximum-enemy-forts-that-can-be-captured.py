class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2511.Maximum%20Enemy%20Forts%20That%20Can%20Be%20Captured
        n = len(forts)
        i = ans = 0
        while i < n:
            j = i + 1
            if forts[i]:
                while j < n and forts[j] == 0:
                    j += 1
                if j < n and forts[i] + forts[j] == 0:
                    ans = max(ans, j - i - 1)
            i = j
        return ans

        # ans = 0
        # i, n = 0, len(forts)
        # while i < n:
        #     if forts[i] == 1:
        #         k = 1
        #         while i + k < n and forts[i+k] == 0:
        #             k += 1
        #         if i + k < n and forts[i+k] == -1:
        #             ans = max(ans, k-1)
        #         k = 1
        #         while i - k >= 0 and forts[i-k] == 0:
        #             k += 1
        #         if i - k >= 0 and forts[i-k] == -1:
        #             ans = max(ans, k-1)
        #     i += 1
        # return ans