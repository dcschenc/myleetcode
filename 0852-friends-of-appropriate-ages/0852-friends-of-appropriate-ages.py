class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counter = Counter(ages)
        total = 0
        for a1 in range(1, 122):
            n1 = counter[a1]
            for a2 in range(int(0.5*a1 + 7 + 1), a1+1):
                n2 = counter[a2]
                total += n1 * n2
                if a1 == a2:
                    total -= n2
        return total


        ages.sort()                                   # sort the `ages`
        ans = 0
        n = len(ages)
        for idx, age in enumerate(ages):              # for each age
            lb = age                                  # lower bound
            ub = (age - 7) * 2                        # upper bound
            i = bisect.bisect_left(ages, lb)          # binary search lower bound
            j = bisect.bisect_left(ages, ub)          # binary search upper bound
            if j - i <= 0: continue
            ans += j - i                              # count number of potential friends
            if lb <= age < ub:                        # ignore itself
                ans -= 1
        return ans


        def binary_search(age):
            left, right = 0, len(ages) - 1
            while left <= right:
                mid = (left + right) // 2
                if ages[mid] > age:
                    right = mid - 1
                else:
                    left = left + 1
            return left
        
        def binary_search_left(age):
            left, right = 0, len(ages) - 1
            while left <= right:
                mid = (left + right) // 2
                if ages[mid] >= age:
                    right = mid - 1
                else:
                    left = left + 1
            return left if ages[left] <= age else left - 1

        age_100 = len([x for x in ages if x > 100])
        ages.sort()
        n = len(ages)
        total = n * (n-1)
        print(total)
        for i in range(n):
            age = 0.5 * ages[i] + 7
            # idx = binary_search_left(age)
            idx = bisect_right(ages, age)
            print('1', idx)
            if idx >= 0:
                total -= (idx)
            # idx = binary_search(ages[i])
            idx = bisect_right(ages, ages[i])
            print(idx)
            if idx <= n:
                total -= (n - idx)
            if ages[i] < 100:
                total -= age_100
        return total

