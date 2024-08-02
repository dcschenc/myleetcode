class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2244.Minimum%20Rounds%20to%20Complete%20All%20Tasks
        counter = Counter(tasks)
        ans = 0
        for k, v in counter.items():
            if v == 1:
                return -1
            ans += v // 3
            if v % 3 != 0:
                ans += 1
        return ans
            
            