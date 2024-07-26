class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        counter = Counter(nums[:k])
        ans.append(len(counter))
        for i in range(k, n):            
            counter[nums[i]] += 1
            if counter[nums[i-k]] == 1:
                del counter[nums[i-k]]
            else:
                counter[nums[i-k]] -= 1
            ans.append(len(counter))
        return ans