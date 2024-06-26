class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def backtrack(nums):
            if len(nums) == 1:
                if abs(nums[0] - 24) < 1e-6:
                # if nums[0] == 24:
                    return True
                return False
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        next_nums = [nums[k] for k in range(n) if k != i and k != j]
                        res = False
                        for op in '+-*/':
                            if op == '/':
                                if nums[j] != 0:
                                    res |= backtrack(next_nums + [nums[i] / nums[j]])
                            elif op == '+':
                                res |= backtrack(next_nums + [nums[i] + nums[j]])
                            elif op == '-':
                                res |= backtrack(next_nums + [nums[i] - nums[j]])
                            else:
                                res |= backtrack(next_nums + [nums[i] * nums[j]])
                        if res:
                            return True
            return False

        res = backtrack(cards)
        return res

