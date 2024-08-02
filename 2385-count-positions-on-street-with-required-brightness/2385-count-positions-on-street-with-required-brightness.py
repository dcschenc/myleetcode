class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2237.Count%20Positions%20on%20Street%20With%20Required%20Brightness
        diff = [0] * (n+1)
        for pos, d in lights:
            left = max(0, pos - d)
            right = min(n-1, pos + d)
            diff[left] += 1
            diff[right + 1] -= 1

        for i in range(1, n+1):
            diff[i] += diff[i-1]

        ans = 0
        for i in range(n):
            if diff[i] >= requirement[i]:
                ans += 1
        return ans

