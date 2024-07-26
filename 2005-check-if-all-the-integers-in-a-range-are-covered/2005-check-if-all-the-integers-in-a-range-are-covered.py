class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1893.Check%20if%20All%20the%20Integers%20in%20a%20Range%20Are%20Covered
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        s = 0
        for i, x in enumerate(diff):
            s += x
            if s == 0 and left <= i <= right:
                return False
        return True


        ranges.sort()
        for start, end in ranges:
            if start <= left <= end:
                left = end + 1
            if left > right:
                return True
        return False

        # for i in range(left, right + 1):
        #     found = False
        #     for l, r in ranges:
        #         if l <= i <= r:
        #             found = True
        #             break
        #     if found == False:
        #         return False
        # return True
