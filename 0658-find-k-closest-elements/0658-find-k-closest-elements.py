class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:       
        if len(arr) == k:
            return arr       
        # We want to search with a window, not for a specific point
        l, r = 0, len(arr) - k
        mid = 0
        while l < r:            
            mid = (l + r) // 2
            # print(l, mid, r)
			#we want to line up mid with the ideal left for our window			
            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1            
            else:
                r = mid
            
		#return the window we have been working with
        return arr[l: l + k]


    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     left, right, length = 0, len(arr)-1, len(arr)
    #     if x < arr[0]:
    #         return arr[:k]
    #     if x > arr[-1]:
    #         return arr[-k:]
    #     pos = -1
    #     while left <= right:
    #         mid = (right+left)//2
    #         # print(mid)
    #         if arr[mid] == x:
    #             pos = mid
    #             break
    #         elif arr[mid] < x and mid+1 < length and arr[mid+1] > x:
    #             pos = mid
    #             if abs(arr[mid] - x) > abs(arr[mid+1] -x ):
    #                 pos = mid + 1
    #             break                
    #         elif arr[mid] < x:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     res = []
  
    #     if pos != -1:
    #         res.append(arr[pos])
    #         left, right = 1, 1
    #         count = 1
    #         while count < k:
    #             if (pos - left) < 0 or (pos + right) > length -1:
    #                 break
    #             if abs(arr[pos-left] - x) <= abs(arr[pos+right] - x):
    #                 res.append(arr[pos-left])
    #                 left += 1
    #             else:
    #                 res.append(arr[pos+right])
    #                 right += 1
    #             count += 1
    #         if count < k:
    #             if (pos - left) < 0:
    #                 while count < k:
    #                     res.append(arr[pos+right])
    #                     count += 1
    #                     right += 1
    #             else:
    #                 while count < k:
    #                     res.append(arr[pos-left])
    #                     count +=1
    #                     left += 1
    #     res.sort()
                
    #     return res

