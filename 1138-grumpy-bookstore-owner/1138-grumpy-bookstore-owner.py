class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1052.Grumpy%20Bookstore%20Owner
        result = current = sum(c for c, g in zip(customers, grumpy) if g == 0)
        for j, (c, g) in enumerate(zip(customers, grumpy)):
            # update right border
            if g == 1:
                current += c            
            # update left border
            i = j - minutes
            if i >= 0 and grumpy[i] == 1:
                current -= customers[i]
            # update answer
            result = max(result, current)
        
        return result

        # total = 0
        # for c, g in zip(customers, grumpy):
        #     if g == 0:
        #         total += c

        # l, i, n = 0, 0, len(customers)
        # mx, cur = 0, 0
        # while i < n:
        #     if i <= minutes:
        #         if grumpy[i] == 1:
        #             cur += customers[i]
        #             mx = cur
        #     else:
        #         if grumpy[l] == 1:
        #             cur -= customers[l]
        #         if grumpy[i] == 1:
        #             cur += customers[i]
        #         l += 1
        #         mx = max(mx, cur)
        #     i += 1
        # return total + mx
