class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # ans = 0
        # for i, num in enumerate(nums):
        #     cnt = bin(i).count('1')
        #     if cnt == k:
        #         ans += num
        # return ans
        
        return sum(x for i, x in enumerate(nums) if i.bit_count() == k)

        ans = 0
        for idx, num in enumerate(nums):
            cnt = 0
            while idx:
                if idx & 1 == 1:
                    cnt += 1
                idx >>= 1
            if cnt == k:
                ans += num
        return ans