class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # l, r = 0, 1
        # res, prev = 1, ""

        # while r < len(arr):
        #     if arr[r - 1] > arr[r] and prev != ">":
        #         res = max(res, r - l + 1)
        #         r += 1
        #         prev = ">"
        #     elif arr[r - 1] < arr[r] and prev != "<":
        #         res = max(res, r - l + 1)
        #         r += 1
        #         prev = "<"
        #     else:
        #         r = r + 1 if arr[r] == arr[r - 1] else r
        #         l = r - 1
        #         prev = ""
        # return res

        max_len = 1
        prev = ''
        cur = 0
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                if prev == '<':
                    cur += 1                    
                else:
                    cur = 2
                prev = '>'
            elif arr[i] < arr[i-1]:
                if prev == '>':
                    cur += 1
                else:
                    cur = 2
                prev = '<'
            else:
                prev = ''
                cur = 0
            max_len = max(max_len, cur)
        return max_len