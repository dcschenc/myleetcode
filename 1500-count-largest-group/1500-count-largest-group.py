class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_counts = {}

        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            digit_sum_counts[digit_sum] = digit_sum_counts.get(digit_sum, 0) + 1

        max_group_size = max(digit_sum_counts.values())
        count_of_max_groups = list(digit_sum_counts.values()).count(max_group_size)

        return count_of_max_groups

        hm = {}
        for i in range(1, n+1):
            total = 0
            while i > 0:
                total += i%10
                i = i//10
            hm[total] = hm.get(total, 0) + 1
            
        sorted_items = sorted(hm.items(), key = lambda x: x[1], reverse=True)
        cnt = 1
        for k, v in sorted_items[1:]:
            if v != sorted_items[0][1]:
                break
            cnt += 1
        return cnt
         
        