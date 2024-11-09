class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
        return sum(nums[:k])

        ans = 0
        if k < numOnes:
            return k
        else:
            ans = numOnes
            k -= numOnes
            
        if k < numZeros:
            return ans
        else:
            k -= numZeros
        
        return ans - k