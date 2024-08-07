class Solution:
    def minMaxDifference(self, num: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2566.Maximum%20Difference%20by%20Remapping%20a%20Digit
        s = str(num)
        mi = int(s.replace(s[0], '0'))
        for c in s:
            if c != '9':
                return int(s.replace(c, '9')) - mi
        return num - mi
        
        # num1 = list(str(num))
        # i, n = 0, len(num1)
        # while i < n:
        #     if num1[i] != '9':
        #         a = num1[i]
        #         num1[i] = '9'
        #         j = i + 1
        #         while j < n:
        #             if num1[j] == a:
        #                 num1[j] = '9'
        #             j += 1
        #         break
        #     i += 1
        # mx = int(''.join(num1))

        # num2 = list(str(num))
        # i, n = 0, len(num2)
        # while i < n:
        #     if num2[i] != '0':
        #         a = num2[i]
        #         num2[i] = '0'
        #         j = i + 1
        #         while j < n:
        #             if num2[j] == a:
        #                 num2[j] = '0'
        #             j += 1
        #         break
        #     i += 1
        # mi = int(''.join(num2))
        # return mx - mi
        