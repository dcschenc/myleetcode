class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2443.Sum%20of%20Number%20and%20Its%20Reverse
        return any(k + int(str(k)[::-1]) == num for k in range(num + 1))

        if num == 0: 
            return True        

        for n1 in range(num):
            n2 = str(n1)
            n2 = n2[::-1]
            n2 = int(''.join(n2))
            if n1 + n2 == num:
                return True
        return False
