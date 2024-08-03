class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2358.Maximum%20Number%20of%20Groups%20Entering%20a%20Competition
        def isPossible(student)->bool:
            if (student * (student + 1)) / 2 <= n:
                return True 
            return False

        n = len(grades)
        low = 1 
        high = n
        while low <= high:
            mid = (low + high) // 2 
            if isPossible(mid) == False:
                high = mid - 1
            else:
                # if isPossible(mid+1) == False:
                #     return mid 
                # else:
                low = mid + 1
        return low - 1
