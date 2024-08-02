class Solution:
    def largestInteger(self, num: int) -> int:
        num_str = str(num)
        even_digits = sorted([int(d) for d in num_str if int(d) % 2 == 0], reverse=True)
        odd_digits = sorted([int(d) for d in num_str if int(d) % 2 != 0], reverse=True)
        
        result = []
        
        even_index = 0
        odd_index = 0
        
        for char in num_str:
            digit = int(char)
            if digit % 2 == 0:
                result.append(even_digits[even_index])
                even_index += 1
            else:
                result.append(odd_digits[odd_index])
                odd_index += 1
        
        return int(''.join(map(str, result)))


        num_str = str(num)
        odd_idx = []
        even_idx = []
        odd, even = '', ''
        for i, c in enumerate(num_str):
            if int(c) % 2 == 1:
                odd_idx.append(i)
                odd += c
            else:
                even_idx.append(i)
                even += c
        odd = sorted(odd, reverse=True)
        even = sorted(even, reverse=True)

        ans = [''] * len(num_str)
        i = 0
        for idx in odd_idx:
            ans[idx] = odd[i]
            i += 1
        i = 0
        for idx in even_idx:
            ans[idx] = even[i]
            i += 1
        return int(''.join(ans))