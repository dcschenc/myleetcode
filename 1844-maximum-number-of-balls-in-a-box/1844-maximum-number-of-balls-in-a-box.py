class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        cnt = [0] * 50
        for x in range(lowLimit, highLimit + 1):
            y = 0
            while x:
                y += x % 10
                x //= 10
            cnt[y] += 1
        return max(cnt)
        
        hm = defaultdict(int)
        max_num = 0
        for i in range(lowLimit, highLimit+1):
            tmp = str(i)
            # tmp = tmp.split()
            # print(tmp)
            box_no = 0
            for c in tmp:
                box_no += int(c)
            hm[box_no] += 1
            # if box_no not in hm:
            #     hm[box_no] = 1
            # else:
            #     hm[box_no] += 1
        return max(hm.values())
        # print(hm)
        # res = []
        # for k, v in hm.items():
            # if v > max_num:
                # max_num = v
            #     res = [k]
            # elif v == max_num:
            #     res.append(k)
            # else:
            #     pass
        # return max_num