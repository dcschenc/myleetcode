class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        t = sorted(set(arr))
        return [bisect_right(t, x) for x in arr]

        
        if len(arr) == 0:
            return []
        sorted_arr = sorted(arr)
        hm = {}
        rank = 1
        hm[sorted_arr[0]] = rank
        for i in range(1, len(sorted_arr)):          
            if sorted_arr[i] != sorted_arr[i-1]:
                rank += 1
                hm[sorted_arr[i]] = rank
        ans = []
        for num in arr:
            ans.append(hm[num])
        return ans

            