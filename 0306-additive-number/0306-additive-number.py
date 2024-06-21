class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)        
        for i in range(1, n):
            for j in range(i+1, n):   
                first = num[:i]                           
                second = num[i:j]        
                if len(first) > 1 and first[0] == '0' or len(second) > 1 and second[0] == '0':
                    continue   
                cur = j
                while cur < n:
                    third = str(int(first) + int(second))
                    if not num.startswith(third, cur):                        
                        break
                    first, second = second, third
                    cur += len(third)
                    if cur == n:
                        return True
        return False

        # n = len(num)
        
        # for i in range(1, n):
        #     for j in range(i+1, n):
        #         first, second = num[:i], num[i:j]

        #         if (len(first) > 1 and first[0] == '0') or (len(second) > 1 and second[0] == '0'):
        #             continue

        #         cur = j
        #         while cur < n:
        #             third = str(int(first) + int(second))
        #             if not num.startswith(third, cur):
        #                 break

        #             cur += len(third)
        #             first, second = second, third

        #             if cur == n:
        #                 return True

        # return False