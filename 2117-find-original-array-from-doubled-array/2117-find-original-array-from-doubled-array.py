from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2007.Find%20Original%20Array%20From%20Doubled%20Array
        n = len(changed)
        if n & 1:
            return []
        cnt = Counter(changed)
        changed.sort()
        ans = []
        for x in changed:
            if cnt[x] == 0:
                continue
            if cnt[x * 2] <= 0:
                return []
            ans.append(x)
            cnt[x] -= 1
            cnt[x * 2] -= 1
        return ans if len(ans) == n // 2 else []
        
        # counter = Counter(changed)
        # changed.sort()
        # ans = []
        # # print(changed)
        # for num in changed:
        #     if num == 0:
        #         if counter[num] >= 2:
        #             ans.append(num)
        #             counter[num] -= 2
        #     elif counter[num] > 0 and num * 2 in counter and counter[num*2] > 0:
        #         ans.append(num)
        #         counter[num] -= 1
        #         counter[num*2] -= 1
        # if len(ans)*2 != len(changed):
        #     return []
        # return ans