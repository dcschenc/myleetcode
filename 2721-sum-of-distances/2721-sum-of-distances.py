class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2615.Sum%20of%20Distances
        ans, n = [], len(nums)
        hm = defaultdict(list)
        presum = defaultdict(list)
        for i, num in enumerate(nums):
            hm[num].append(i)
            if num not in presum:
                presum[num] = [0]
            presum[num].append(presum[num][-1] + i)
                        
        for i in range(n):
            num = nums[i]
            seq = hm[num]
            idx = bisect_left(seq, i)
            left = idx * i - presum[num][idx]
            idx = bisect_right(seq, i)
            right = presum[num][len(seq)] - presum[num][idx] - i * (len(seq) - idx)
            ans.append(left + right)
        return ans