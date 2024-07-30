class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2131.Longest%20Palindrome%20by%20Concatenating%20Two%20Letter%20Words
        counter = Counter(words)
        keys = set(counter.keys())
        ans = 0
        same_ans = False
        for k in keys:
            if k[0] == k[1]:
                ans += 4 * (counter[k] // 2)
                if counter[k] % 2 == 1:
                    same_ans = True
            else:
                n_key = k[::-1]
                if n_key in keys:
                    ans += min(counter[k], counter[n_key]) * 2
                    
        return ans + 2 if same_ans else ans
        