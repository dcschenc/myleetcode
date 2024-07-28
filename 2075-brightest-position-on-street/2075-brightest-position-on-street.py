class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2021.Brightest%20Position%20on%20Street
        min_idx, max_idx = float(inf), -float(inf)
        for i in range(len(lights)):
            left = lights[i][0] - lights[i][1]
            right = lights[i][0] + lights[i][1]
            lights[i][0], lights[i][1] = left, right
            # min_idx = min(min_idx, left)
            # max_idx = max(max_idx, right)
        # n = max_idx - min_idx + 1
        # diff = [0] * (n + 1)
        diff = defaultdict(int)
        for start, end in lights:
            diff[start] += 1
            diff[end + 1] -= 1
        cur, max_val, ans = 0, 0, 0
        for k in sorted(diff):
            cur += diff[k]
            if cur > max_val:
                max_val = cur
                ans = k
        return ans
        
        
