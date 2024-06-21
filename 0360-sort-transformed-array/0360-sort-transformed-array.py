class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a * x**2 + b * x + c

        n = len(nums)
        result = [0] * n

        i, j = 0, n - 1
        index = n - 1 if a >= 0 else 0

        while i <= j:
            if a >= 0:
                if quadratic(nums[i]) >= quadratic(nums[j]):
                    result[index] = quadratic(nums[i])  
                else:
                    result[index] = quadratic(nums[j])
                index -= 1
            else:
                if quadratic(nums[i]) <= quadratic(nums[j]):
                    result[index] = quadratic(nums[i])  
                else:
                    result[index] = quadratic(nums[j])
                index += 1

            if a >= 0:
                if quadratic(nums[i]) >= quadratic(nums[j]):
                    i += 1
                else:
                    j -= 1
            else:
                if quadratic(nums[i]) <= quadratic(nums[j]):
                    i += 1
                else:
                    j -= 1

        return result