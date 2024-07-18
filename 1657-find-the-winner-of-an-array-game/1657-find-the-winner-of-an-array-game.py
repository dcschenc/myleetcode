class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1535.Find%20the%20Winner%20of%20an%20Array%20Game
        mx = arr[0]
        cnt = 0
        for x in arr[1:]:
            if mx < x:
                mx = x
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                break
        return mx
        
        n = len(arr)
        i, mx = 0, 0
        while i < n:
            j = i
            while j + 1 < n and arr[j + 1] < arr[i]:
                j += 1
            count = j - i
            if i > 0 and arr[i] > mx:
                count += 1
            if count >= k:
                return arr[i]
            mx = max(mx, arr[i])
            i += 1
        return mx