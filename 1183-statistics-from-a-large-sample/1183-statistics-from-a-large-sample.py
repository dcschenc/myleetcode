class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        largest = -1
        mx, mi, mode, total, cnt = -1, 256, -1, 0, 0
        counter = []
        for i, num in enumerate(count):
            if num != 0:
                total += i * num
                cnt += num
                mx = max(mx, i)
                mi = min(mi, i)
                if num > largest:
                    largest = num
                    mode = i
                counter.append((num, i))
        mean = total / cnt
        mid = cnt // 2
        if cnt % 2 == 1:
            mid = mid + 1
        cur = 0
        for i, (c, num) in enumerate(counter):
            if cur + c < mid:
                cur += c
                continue
            if cur + c > mid:
                median = num
            elif cur + c == mid:
                if cnt % 2 == 1:
                    median = num
                else:
                    median = (num + counter[i+1][1]) / 2
            break
        return [mi, mx, mean, median, mode]
