class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countPartitions(maxSum):
            partitions = 1
            subSum = 0
            for num in nums:
                if subSum + num <= maxSum:
                    subSum += num
                else:
                    partitions += 1
                    subSum = num
            return partitions

        low = max(nums)
        high = sum(nums)
        while low <= high:
            mid = (low + high) // 2
            partitions = countPartitions(mid)
            if partitions > k:
                low = mid + 1
            else:
                high = mid - 1
        return low        