class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2610.Convert%20an%20Array%20Into%20a%202D%20Array%20With%20Conditions
        # cnt = Counter(nums)
        # ans = []
        # for x, v in cnt.items():
        #     for i in range(v):
        #         if len(ans) <= i:
        #             ans.append([])
        #         ans[i].append(x)
        # return ans

        counter = Counter(nums)
        ans, total, cnt = [], len(nums), 0
        while cnt < total:
            row = []
            for key in list(counter.keys()):
                if counter[key] > 0:
                    row.append(key)
                    counter[key] -= 1
                    cnt += 1  
                else:
                    # del counter[key]          
                    counter.pop(key)
            ans.append(row)
        return ans
