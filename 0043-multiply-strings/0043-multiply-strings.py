class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = 0
        hm = {}
        for i, n2 in enumerate(num2[::-1]):
            for j, n1 in enumerate(num1[::-1]) :
                if n1 == 0 or n2 == 0:
                    continue
                res += int(n2) * int(n1) * pow(10, i  + j)
                # if n2 + n1 in hm:
                #     res += hm[n2+n1] * pow(10, i+j)
                # else:
                #     tmp = int(n2) * int(n1)
                #     hm[n2+n1] = tmp
                #     res += hm[n2+n1] * pow(10, i+j)
        return str(res)
