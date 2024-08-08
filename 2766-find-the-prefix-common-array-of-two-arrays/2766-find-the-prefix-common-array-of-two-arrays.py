class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2657.Find%20the%20Prefix%20Common%20Array%20of%20Two%20Arrays
        seta, setb = set(), set()
        n = len(A)
        ans = []
        for i in range(n):
            seta.add(A[i])
            setb.add(B[i])
            add = 0
            if A[i] in setb:
                add += 1
            if B[i] in seta:
                add += 1
            if A[i] == B[i]:
                add -= 1
            if i == 0:
                ans.append(add)
            else:
                ans.append(add + ans[-1])
        return ans
