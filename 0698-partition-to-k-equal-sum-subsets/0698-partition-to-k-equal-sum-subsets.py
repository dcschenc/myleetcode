class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # https://github.com/doocs/leetcode/blob/main/solution/0600-0699/0698.Partition%20to%20K%20Equal%20Sum%20Subsets/README.md
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if j and cur[j] == cur[j - 1]:
                    continue
                cur[j] += nums[i]
                if cur[j] <= s and dfs(i + 1):
                    return True
                cur[j] -= nums[i]
            return False

        s, mod = divmod(sum(nums), k)
        if mod: return False
        cur = [0] * k
        nums.sort(reverse=True)
        return dfs(0)


        # def backtrack(idx):            
        #     nonlocal limit
        #     if idx == len(nums):
        #         if len(set(subset)) == 1:
        #             return True
        #         return False            
        #     for i in range(k):
        #         if subset[i] + nums[idx] >= limit or i > 0 and subset[i] == subset[i-1]:  ### pruning
        #             continue
        #         subset[i] += nums[idx]
        #         res = backtrack(idx + 1)
        #         if res is True:
        #             return True
        #         subset[i] -= nums[idx]
        #     return False        

        # nums.sort(reverse=True)
        # if sum(nums) % k != 0:
        #     return False
        # limit = sum(nums) // k + 1
        # subset = [0] * k
        # res = backtrack(0)
        # return res

        