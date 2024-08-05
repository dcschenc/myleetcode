class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2433.Find%20The%20Original%20Array%20of%20Prefix%20Xor
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(pref[i-1] ^ pref[i])
        return ans