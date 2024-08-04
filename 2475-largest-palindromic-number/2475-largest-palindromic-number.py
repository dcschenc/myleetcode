class Solution:
    def largestPalindromic(self, num: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2384.Largest%20Palindromic%20Number
        counter = Counter(num)
        left, right = '', ''
        single = ''
        for k, v in sorted(counter.items(), reverse=True):
            if v % 2 == 1 and single == '':
                single = k
            if k == '0' and len(left) == 0:
                continue            
            left += k * ( v // 2)
            right += k * (v // 2)

        right = right[::-1]
        return left + single + right if left + single + right != '' else '0'

        # counter = Counter(num)
        # left, right = '', ''
        # single = ''
        # for k in sorted(counter.keys(), reverse=True):
        #     cnt = counter[k]
        #     if cnt % 2 == 1 and single == '':
        #         single = k
        #     if k == '0' and len(left) == 0:
        #         continue            
        #     left += k * ( cnt // 2)
        #     right += k * (cnt // 2)

        # right = right[::-1]
        # return left + single + right if left + single + right != '' else '0'