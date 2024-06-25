class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0567.Permutation%20in%20String
        n = len(s1)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:n])
        if cnt1 == cnt2:
            return True
        for i in range(n, len(s2)):
            cnt2[s2[i]] += 1
            cnt2[s2[i - n]] -= 1
            if cnt1 == cnt2:
                return True
        return False