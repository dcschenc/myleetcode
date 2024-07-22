class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1679.Max%20Number%20of%20K-Sum%20Pairs
        hm = {}
        count = 0
        for n in nums:
            if k-n in hm and hm.get(k-n) > 0:
                count += 1
                hm[k-n] -= 1
            else:
                hm[n] = 1 + hm.get(n, 0)
        return count

        ####### O(nlogn) #####
        # nums.sort()
        # i, j = 0, len(nums)-1
        # count = 0
        # while i < j:
        #     sum_ = nums[i] + nums[j]
        #     if sum_ == k:
        #         count += 1
        #         i+=1
        #         j-=1
        #     elif sum_ < k:
        #         i+=1
        #     else:
        #         j-=1
        # return count