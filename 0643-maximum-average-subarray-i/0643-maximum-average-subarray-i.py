class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        s = sum(nums[:k])
        answer = s
        for i in range(k, n):
            s += nums[i]
            s -= nums[i-k]
            answer = max(answer, s)
        return answer/k
        # max_avg = last_avg = mean(nums[:k])
        # n = len(nums)
        # idx = 0
        # for i in range(k, n):
        #     new_avg = last_avg + (nums[i]-nums[i-k])/k
        #     last_avg = new_avg
        #     if new_avg > max_avg:
        #         max_avg = new_avg
        # return max_avg
