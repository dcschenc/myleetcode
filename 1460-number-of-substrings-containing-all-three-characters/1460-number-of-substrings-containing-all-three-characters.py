from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1358.Number%20of%20Substrings%20Containing%20All%20Three%20Characters
        d = {"a": -1, "b": -1, "c": -1}
        ans = 0
        for i, c in enumerate(s):
            d[c] = i
            ans += min(d["a"], d["b"], d["c"]) + 1
        return ans

        n = len(s)
        count = 0
        char_count = [0, 0, 0] 
        left = 0 

        for right in range(n):
            char_count[ord(s[right]) - ord('a')] += 1  
            while all(char_count):
                char_count[ord(s[left]) - ord('a')] -= 1
                left += 1
            # Add the count of substrings ending at the current position
            count += left

        return count