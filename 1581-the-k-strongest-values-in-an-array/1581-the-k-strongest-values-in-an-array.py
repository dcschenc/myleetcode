class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) >> 1]
        arr.sort(key=lambda x: (abs(x - m), x), reverse=True)
        return arr[:k]

        # arr.sort()
        # n = len(arr)
        # m = arr[(n-1)//2]
        # i, j = 0, len(arr)-1
        # ans = []
        # while i <= j:            
        #     diff = abs(arr[i] - m) - abs(arr[j] - m)
        #     if diff > 0:                
        #         ans.append(arr[i])
        #         i += 1
        #     elif diff == 0:
        #         if arr[i] > arr[j]:                    
        #             ans.append(arr[i])
        #             i += 1
        #         elif arr[i] <= arr[j]:                    
        #             ans.append(arr[j])
        #             j -= 1
        #     else:
        #         ans.append(arr[j])
        #         j -= 1
        # return ans[:k]