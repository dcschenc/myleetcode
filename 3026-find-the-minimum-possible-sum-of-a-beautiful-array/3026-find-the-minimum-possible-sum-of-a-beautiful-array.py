class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2834.Find%20the%20Minimum%20Possible%20Sum%20of%20a%20Beautiful%20Array
        mod = 10**9 + 7
        m = target // 2
        if n <= m:
            return ((1 + n) * n // 2) % mod
        return ((1 + m) * m // 2 + (target + target + n - m - 1) * (n - m) // 2) % mod


        # #basic idea: use sum of contiguous integer formula
        # #we need a left_sum and in most cases, a right_sum
        # #return the sum of two separate arrays: left_sum = sum(1, target//2), right_sum = sum(target, n - left_sum)
        
        half_target = target//2
        left_sum_first_term = 1
        left_sum_second_term = min(n, half_target)
        left_sum_len = min(n, half_target)

        def get_sum_contiguous_integers(first_term, second_term, length):
            return length * (first_term + second_term) // 2

        left_sum = get_sum_contiguous_integers(left_sum_first_term, left_sum_second_term, left_sum_len)
        
        if half_target >= n:
            return left_sum

        right_sum_len = n - half_target
        right_sum_first_term = target
        right_sum_second_term = target + n - left_sum_len - 1

        right_sum = get_sum_contiguous_integers(right_sum_first_term, right_sum_second_term, right_sum_len)

        return (left_sum + right_sum) % (10 ** 9 + 7)

        if n == 1:
            return (1)
        elif n < target // 2:
            return n * (n + 1) // 2
        else:
            a = target // 2
            ans = a * (a + 1) // 2
            b = target 
            c = target + (n - a-1)
            second = (c-b+1)*(c+b)//2
            final = ans + second
            # rem = target - a - 1
            # add = n + rem
            # final = (add * (add + 1) // 2) - ((target - 1) * target // 2) + ans
            return (final) % (10**9 + 7)

        cur, cnt, ans = 1, 0, 0
        while cnt != min(target//2, n):
            ans += cur
            cnt += 1
            cur += 1   
        if cnt == n: 
            return ans % (10 ** 9 + 7)

        ans += (n//2) * (target + n//2 - 1 + target)//2
        # cur = target         
        # while cnt != n:
        #     ans += cur
        #     cur += 1
        #     cnt += 1
        return ans % (10 ** 9 + 7)

        cur, cnt = 1, 0
        hm = set()
        while cnt != n:
            if cur not in hm and target - cur not in hm:
                hm.add(cur)
                cnt += 1
            cur += 1            
        return sum(hm) % (10 ** 9 + 7)