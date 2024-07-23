class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1711.Count%20Good%20Meals
        powers_of_two = [2**i for i in range(22)]
        counter = {}
        result = 0

        for num in deliciousness:
            for power in powers_of_two:
                complement = power - num
                if complement in counter:
                    result += counter[complement]
            counter[num] = counter.get(num, 0) + 1

        return result % (10**9 + 7)

        # def is_2_power(x):            
        #     cur = 1
        #     while cur <= x:
        #         if cur == x:
        #             return True
        #         cur *= 2
        #     return False

        # counter = Counter(deliciousness)
        # keys = counter.keys()
        # ans = 0
        # for a, b in combinations(keys, 2):            
        #     if is_2_power(a + b):
        #         ans += counter[a] * counter[b]
        # print(counter)
        # for k in keys:
        #     if counter[k] > 1 and is_2_power(k + k):
        #         ans += counter[k] * (counter[k] - 1) // 2

        # return ans % (10**9 + 7)