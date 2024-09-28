class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1456.Maximum%20Number%20of%20Vowels%20in%20a%20Substring%20of%20Given%20Length
        vowels = set("aeiou")
        ans = cnt = sum(c in vowels for c in s[:k])
        for i in range(k, len(s)):
            cnt += int(s[i] in vowels) - int(s[i - k] in vowels)
            ans = max(ans, cnt)
        return ans


        # max_n, last_n = 0, 0
        # n = len(s)
        # for i in range(k):
        #     if s[i] in ['a', 'e', 'i', 'o', 'u']:
        #         max_n += 1
        # last_n = max_n
        # for i in range(k, n):
        #     if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
        #         last_n -= 1
        #     if s[i] in ['a', 'e', 'i', 'o', 'u']:
        #         last_n += 1
        #     if last_n > max_n:
        #         max_n = last_n
        # return max_n