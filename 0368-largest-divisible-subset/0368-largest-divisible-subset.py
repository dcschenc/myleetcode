class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        f = [1] * n
        k = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    f[i] = max(f[i], f[j] + 1)
            if f[k] < f[i]:
                k = i
        m = f[k]
        i = k
        ans = []
        while m:
            if nums[k] % nums[i] == 0 and f[i] == m:
                ans.append(nums[i])
                k, m = i, m - 1
            i -= 1
        return ans

        
        nums.sort()
        candidates = []
        for i, num in enumerate(nums):
            found = False
            for j in range(len(candidates)):
                if num % (candidates[j][-1]) == 0:
                    new_candidate = candidates[j].copy()
                    new_candidate.append(num)
                    candidates.append(new_candidate)
                    found = True                
            if found is False:
                candidates.append([num])
        #     print(num, candidates)
        # print(nums)
        # print(candidates)
        max_cnt = 0
        for candidate in candidates:
            if max_cnt < len(candidate):
                ans = candidate
                max_cnt = len(candidate)
        return ans
