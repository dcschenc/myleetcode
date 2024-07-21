class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1604.Alert%20Using%20Same%20Key-Card%20Three%20or%20More%20Times%20in%20a%20One%20Hour%20Period
        hm = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            hm[name].append(time)
            
        ans = []
        for name, times in hm.items():
            if len(times) < 3:
                continue
            times.sort()
            for i in range(len(times) - 2):                
                t1 = times[i]
                t2 = times[i + 2]
                h1, h2 = int(t1[:2]), int(t2[:2])
                if h1 == h2:
                    ans.append(name)
                    break
                if h2 - h1 == 1:
                    m1, m2 = int(t1[3:]), int(t2[3:])
                    if 60 - m1 + m2 <= 60:
                        ans.append(name)
                        break
        ans.sort()
        return ans
            