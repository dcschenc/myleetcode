class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int: 
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0923.3Sum%20With%20Multiplicity   
        cnt = Counter(arr)
        ans = 0
        mod = 10**9 + 7
        for j, b in enumerate(arr):
            cnt[b] -= 1
            for i in range(j):
                a = arr[i]
                c = target - a - b
                ans = (ans + cnt[c]) % mod
        return ans

    
        # counter = Counter(arr)
        # if len(counter) == 1 and sum(arr[:3]) == target:
        #     return math.comb(len(arr), 3)% (10**9 + 7)
        # arr.sort()
        # n = len(arr)
        # ans = 0
        # for i in range(n):
        #     j, k = i + 1, n-1
        #     while j <= k:
        #         s = arr[i] + arr[j] + arr[k]                
        #         if s == target:                                     
        #             cntj, cntk = 1, 1
        #             if arr[j] != arr[k]:
        #                 while j + 1 < k and arr[j+1] == arr[j]:
        #                     cntj += 1
        #                     j += 1
        #                 while k - 1 > j and arr[k-1] == arr[k]:
        #                     cntk += 1
        #                     k -= 1
        #                 ans += cntj * cntk
        #                 j += 1
        #                 k -= 1
        #             else:
        #                 ans += (k-j+1) * (k-j)//2
        #                 break                                      
        #         elif s > target:
        #             k = k - 1
        #         else:
        #             j = j + 1     
        # return ans