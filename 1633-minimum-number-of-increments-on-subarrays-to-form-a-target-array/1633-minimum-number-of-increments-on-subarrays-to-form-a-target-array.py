class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1526.Minimum%20Number%20of%20Increments%20on%20Subarrays%20to%20Form%20a%20Target%20Array

        return target[0] + sum(max(0, b - a) for a, b in pairwise(target))
        
        increments = target[0]        
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                increments += target[i] - target[i - 1]
        
        return increments