class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

        # res = []
        # add_one = True
        # for i in range(len(digits)-1, -1,-1):
        #     if add_one is True:
        #         if digits[i] + 1 <10:
        #             res.append(digits[i] + 1)
        #             add_one = False
        #         else:
        #             res.append(0)
        #     else:
        #         res.append(digits[i])
        # if add_one is True:
        #     res.append(1)
        # return res[::-1]