class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2575.Find%20the%20Divisibility%20Array%20of%20a%20String
        ans = []
        x = 0
        for c in word:
            x = (x * 10 + int(c)) % m
            ans.append(1 if x == 0 else 0)
        return ans
                
        # n = len(word)
        # ans = [0] * n
        # pre = [0] * n
        # for i in range(len(word)):
        #     if i == 0:
        #         pre[i] = int(word[i]) % m
        #     else:
        #         pre[i] = (pre[i-1] + int(word[i])) % m

        #     if pre[i] == 0:
        #         ans[i] = 1
        # return ans