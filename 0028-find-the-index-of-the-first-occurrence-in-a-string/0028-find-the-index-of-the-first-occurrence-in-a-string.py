class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for i in range(len(haystack)-len(needle)+1):
        #     if haystack[i:i+len(needle)] == needle:
        #         return i
        # return -1

        if needle == haystack:
            return 0
        i = 0
        j = len(needle)
        while j <= len(haystack):
            currentNeedle = haystack[i:j]
            if currentNeedle == needle:
                return i
            i += 1
            j += 1
        return -1