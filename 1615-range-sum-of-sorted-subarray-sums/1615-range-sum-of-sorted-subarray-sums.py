class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1508.Range%20Sum%20of%20Sorted%20Subarray%20Sums
        arr = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                arr.append(s)
        arr.sort()
        mod = 10**9 + 7
        return sum(arr[left - 1 : right]) % mod


        sub_sum = []
        prev = []
        for i in range(len(nums)):
            cur = []
            if i == 0:
                cur.append(nums[0])
                for j in range(1, len(nums)):
                    cur.append(nums[j] + cur[-1])
            else:
                for j in range(1, len(prev)):
                    cur.append(prev[j] - prev[0])
            sub_sum.extend(cur)
            prev = cur
        # print(sub_sum)
        sub_sum.sort()
        return sum(sub_sum[left-1: right])% (10**9 + 7)
