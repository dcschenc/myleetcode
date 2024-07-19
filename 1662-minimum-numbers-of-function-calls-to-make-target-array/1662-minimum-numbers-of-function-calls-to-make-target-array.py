class Solution:
    def minOperations(self, nums: List[int]) -> int:
        add, multiple = 0, 0
        for num in nums:
            times = 0
            while num > 0:
                if num % 2 == 0:
                    num = num // 2
                    times += 1
                else:
                    num -= 1
                    add += 1
            multiple = max(multiple, times)
        return add + multiple

        add, multiple = 0, 0
        for num in nums:
            times = floor(math.log(num, 2))
            multiple = max(multiple, times)
            add += num - 2 ** times + 1
        return add + multiple