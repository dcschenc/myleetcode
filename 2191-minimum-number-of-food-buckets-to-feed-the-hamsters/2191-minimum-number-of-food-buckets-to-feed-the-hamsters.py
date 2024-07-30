class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2086.Minimum%20Number%20of%20Food%20Buckets%20to%20Feed%20the%20Hamsters
        ans = 0
        i, n = 0, len(hamsters)
        while i < n:
            if hamsters[i] == 'H':
                if i + 1 < n and hamsters[i + 1] == '.':
                    i += 2
                    ans += 1
                elif i and hamsters[i - 1] == '.':
                    ans += 1
                else:
                    return -1
            i += 1
        return ans

        hamsters = list(hamsters)
        cost = 0
        n = len(hamsters)
        for i, c in enumerate(hamsters):
            if c == 'H':
                if i == 0:
                    if i + 1 < n and hamsters[i+1] == '.':
                        hamsters[i+1] = 'f'
                        cost += 1
                    else:
                        return -1
                else:                    
                    if hamsters[i-1] == 'f':
                        continue
                    else:
                        if i + 1 < n and hamsters[i+1] == '.':
                            hamsters[i+1] = 'f'
                            cost += 1
                        else:
                            if hamsters[i-1] == '.':
                                cost += 1
                            else:
                                return -1

        return cost

