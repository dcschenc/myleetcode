class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0845.Longest%20Mountain%20in%20Array
        n = len(arr)
        f = [1] * n
        g = [1] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                f[i] = f[i - 1] + 1
        ans = 0
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                g[i] = g[i + 1] + 1
                if f[i] > 1:
                    ans = max(ans, f[i] + g[i] - 1)
        return ans


        n = len(arr)
        ans = l = 0
        while l + 2 < n:
            r = l + 1
            if arr[l] < arr[r]:
                while r + 1 < n and arr[r] < arr[r + 1]:
                    r += 1
                if r < n - 1 and arr[r] > arr[r + 1]:
                    while r < n - 1 and arr[r] > arr[r + 1]:
                        r += 1
                    ans = max(ans, r - l + 1)
                else:
                    r += 1
            l = r
        return ans

        n = len(arr)
        max_length = 0

        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:
                left = i - 1
                right = i + 1

                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                max_length = max(max_length, right - left + 1)

        return max_length

        n = len(arr)
        left, i = 0, 1
        ans = 0
        peak = False
        is_increase = False    
        while i < n:
            if arr[i] == arr[i-1]:                
                if peak is True:
                    ans = max(ans, i-left)
                left = i
                is_increase = False
                peak = False
            elif arr[i] < arr[i-1]:
                if is_increase == True:
                    peak = True
                else:
                    left = i
                if i == n-1 and is_increase == True:
                    ans = max(ans, i-left+1)
            else:
                is_increase = True
                if peak == True:
                    ans = max(ans, i-left)
                    left = i-1
                    peak = False
            i += 1
        return ans

