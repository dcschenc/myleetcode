class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1441.Build%20an%20Array%20With%20Stack%20Operations   
        cur, ans = 0, []
        for v in target:
            cur += 1
            while cur < v:
                ans.extend(['Push', 'Pop'])
                cur += 1
            ans.append('Push')
        return ans


        # ans = []
        # stack = []
        # idx, n = 0, len(target)
        # cur = 1
        # while idx < n:
        #     if target[idx] > cur:
        #         ans.append("Push")
        #         ans.append('Pop')
        #     elif target[idx] == cur:
        #         ans.append("Push")
        #         idx += 1
        #     cur += 1
        # return ans


