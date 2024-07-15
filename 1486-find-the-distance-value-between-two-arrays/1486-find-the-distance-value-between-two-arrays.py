class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0        
        for a in arr1:
            # Find the smallest element in arr2 that is >= a - d
            left = bisect.bisect_left(arr2, a - d)
            # Find the largest element in arr2 that is <= a + d
            right = bisect.bisect_right(arr2, a + d)
            
            # Check if any element in arr2 within range [a - d, a + d]
            if left == right:
                count += 1
        
        return count

        # count=0
        # arr2.sort()
        # for i in range(len(arr1)):
        #     left,right=0,len(arr2)-1
        #     while left<=right:
        #         mid=(left+right)//2
        #         if abs(arr1[i]-arr2[mid])<=d:
        #             count+=1
        #             break
        #         elif arr1[i]<arr2[mid]:
        #             right=mid-1
        #         else:
        #             left=mid+1
        # return len(arr1)-count
        
        # def check(num: int) -> bool:
        #     i = bisect_left(arr2, num - d)
        #     return i == len(arr2) or arr2[i] > num + d

        # ans = 0
        # arr2.sort()
        # for num in arr1:
        #     ans += check(num)
        # return ans

        # count = 0
        # arr2.sort()
        # for num1 in arr1:
        #     check = True
        #     for num2 in arr2:
        #         if abs(num1-num2) <= d:
        #             check = False
        #             break    
        #     if check:
        #         count += 1
        # return count        