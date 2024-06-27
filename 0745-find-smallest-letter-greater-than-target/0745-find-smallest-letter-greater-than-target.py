class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target>=letters[-1]:
            return letters[0]
        left,right=0,len(letters)-1
        while left<=right:
            mid=(right+left)//2
            if letters[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        return letters[left]
    
        # while left<=right:
        #     mid = (left+right)//2
        #     if letters[mid] == target and (mid+1) < len(letters) and letters[mid] != letters[mid+1]:
        #         return letters[mid+1]
        #     elif ord(letters[mid]) < target_ord and (mid+1) < len(letters) and ord(letters[mid+1]) > target_ord:
        #         return letters[mid+1]
        #     elif ord(letters[mid]) <= target_ord:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return letters[0]
                