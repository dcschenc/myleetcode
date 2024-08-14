class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2933.High-Access%20Employees
        d = defaultdict(list)
        for name, t in access_times:
            d[name].append(int(t[:2]) * 60 + int(t[2:]))
        ans = []
        for name, ts in d.items():
            ts.sort()
            if any(ts[i] - ts[i - 2] < 60 for i in range(2, len(ts))):
                ans.append(name)
        return ans

        # def in_one_hour(time1, time2):
        #     h1, h2 = int(time1[:2]), int(time2[:2])
        #     m1, m2 = int(time1[2:]), int(time2[2:])
        #     if h1 == h2 and m1 - m2 < 60 or h1 - h2 == 1 and 60 - m2 + m1 < 60:
        #         return True
        #     return False
                
        # hm = defaultdict(list)
        # for u, t in access_times:
        #     hm[u].append(t)
        # ans = []
        # for k, times in hm.items():
        #     times.sort()
        #     n = len(times)
        #     i = 0
        #     while i < n:
        #         j = i + 1
        #         while j < n and in_one_hour(times[j], times[i]):
        #             j += 1
        #         if j - i >= 3:
        #             ans.append(k)
        #             break
        #         i += 1
        # return ans