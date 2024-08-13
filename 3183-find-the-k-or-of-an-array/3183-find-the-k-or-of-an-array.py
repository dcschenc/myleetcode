class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2917.Find%20the%20K-or%20of%20an%20Array
        ans = 0
        for i in range(31):  ### positive number
            cnt = 0
            for num in nums:
                if num >> i & 1:
                    cnt += 1
            if cnt >= k:
                ans |= (1 << i)
        return ans