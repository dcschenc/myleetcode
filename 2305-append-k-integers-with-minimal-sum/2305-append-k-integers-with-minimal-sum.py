class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2195.Append%20K%20Integers%20With%20Minimal%20Sum
        nums.extend([0, 2 * 10**9])
        nums.sort()
        ans = 0
        for a, b in pairwise(nums):
            m = max(0, min(k, b - a - 1))
            ans += (a + 1 + a + m) * m // 2
            k -= m
        return ans

        nums.append(0)
        nums.sort()
        ans = 0        
        nums.append(2 * 10**9)
        for i in range(1, len(nums)):
            start, end = nums[i-1], nums[i]
            n = end - start - 1
            if n <= 0:
                continue
            n = min(n, k)
            k -= n
            ans += (start + 1 + start + n) * n // 2            
            if k == 0:
                break       
        return ans

        # hm = set(nums)
        # cur, ans = 1, 0
        # mx = max(nums)
        # while k > 0:
        #     if cur > mx:               
        #         ans += k * (2 * cur +k - 1) // 2
        #         return ans                
        #     if cur not in hm:
        #         # hm.add(cur)
        #         ans += cur
        #         k -= 1
        #     cur += 1
        # return ans
