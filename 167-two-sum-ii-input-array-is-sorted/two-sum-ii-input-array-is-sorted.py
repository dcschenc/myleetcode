class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1
        while L < R:
            cur = numbers[L] + numbers[R]
            if cur == target:
                return [L+1, R+1]
            elif cur > target:
                R -= 1
            else:
                L += 1