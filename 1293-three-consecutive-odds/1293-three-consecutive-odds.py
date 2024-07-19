class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt, n = 0, len(arr)
        for i in range(n):
            if arr[i] % 2 == 1:
                cnt += 1
                if cnt == 3: return True
            else:
                cnt = 0
        return False
        
        # for i in range(1, len(arr) - 1):
        #     if arr[i] % 2 == 1 and arr[i-1] % 2 == 1 and arr[i+1]%2 == 1:
        #         return True
        # return False