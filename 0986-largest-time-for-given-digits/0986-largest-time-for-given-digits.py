class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:     
        mx = ''
        for a, b, c, d in permutations(arr, 4):
            if c * 10 + d >= 60: continue
            time = str(a) + str(b) + ":" + str(c) + str(d)
            if '00:00' <= time <= '23:59' and (time > mx or mx == ''):
                mx = time
        return mx

        # mx = ''
        # arr = Counter(arr)
        # for h in range(24):
        #     for m in range(60):
        #         time = f"{h:02d}:{m:02d}"
        #         if Counter([int(time[0]), int(time[1]), int(time[3]), int(time[4])]) == arr:
        #             if '00:00' <= time <= '23:59' and (time > mx or mx == ''):
        #                 mx = time
        # return mx

